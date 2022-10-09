import logging
import typing as t
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)
class_registry: t.Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: t.Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def read(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Read single listing
        :param db: DB session
        :param id: ID of record to be fetched
        :return: Record instance
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def read_all(
            self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Read all listing. Limit results via skip and limit parameters
        :param db: DB session
        :param skip: How many records will be skipped from results
        :param limit: How many listings will be returned
        :return: Sequence of record instances
        """
        result = db.query(self.model).offset(skip).limit(limit).all()
        logger.info(result)
        return result

    def get_new_id(self, db: Session):
        """
        Get an id for new record based on existing records
        :param db: DB session
        :return: new id
        """
        result = db.query(self.model).order_by(self.model.id.desc()).first()
        if not result:
            return 0
        else:
            return result.id + 1

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Creates new instance using given object
        :param db: DB session
        :param obj_in: Input object will be created
        :return: Created instance
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db_obj.id = self.get_new_id(db=db)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        Updates instance of given id with values of new object
        :param db: DB session
        :param db_obj: Existing object
        :param obj_in: New object
        :return: Updated instance
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> ModelType:
        """
        Delte object with given id
        :param db: DB session
        :param id: ID of instance
        :return: Deleted instance
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
