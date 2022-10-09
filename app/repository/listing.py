from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.db.base import CRUDBase
from app.model.listing import Listing
from app.schema.listing import ListingCreateSchema, ListingUpdateSchema


class ListingRepository(CRUDBase[Listing, ListingCreateSchema, ListingUpdateSchema]):
    def search(
            self, db: Session, *, keyword: str, limit: int = 100
    ) -> List[Listing]:
        """
        Returns listing which contains keyword in address field.
        :param db: DB session
        :param keyword: Search keyword
        :param limit: How many results will be returned
        :return: List of listing instance
        """
        results = db.query(self.model).filter(func.lower(self.model.address).contains(keyword.lower())).limit(limit).all()
        return results




