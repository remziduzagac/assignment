from pydantic import BaseModel


class ListingBaseSchema(BaseModel):
    id: int
    address: str
    price: float


class ListingSchema(ListingBaseSchema):
    class Config:
        orm_mode = True


class ListingCreateSchema(BaseModel):
    address: str
    price: float


class ListingUpdateSchema(ListingBaseSchema):
    pass
