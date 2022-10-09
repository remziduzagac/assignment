from typing import Any, Optional, Sequence

from fastapi import APIRouter, Depends, Query, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.db.session import get_db
from app.model.listing import Listing
from app.repository.listing import ListingRepository
from app.schema.generic import Message
from app.schema.listing import ListingSchema, ListingCreateSchema, ListingUpdateSchema

router = APIRouter()
listingRepo = ListingRepository(Listing)


@router.get("/{id}", status_code=200, response_model=ListingSchema, responses={404: {"model": Message}})
async def get_listing(
        *,
        id: int = Path(title="ID of listing to be fetched"),
        db: Session = Depends(get_db)
) -> Any:
    """
    Fetch a single listing by ID
    """
    result = listingRepo.read(db=db, id=id)
    if not result:
        return JSONResponse(
            status_code=404, content={"message": f"Listing with ID {id} not found"}
        )
    else:
        return result


@router.get("/", status_code=200, response_model=Sequence[ListingSchema], responses={404: {"model": Message}})
async def get_listings(
        *,
        skip: Optional[int] = Query(default=0, title="How many listings will be skipped from results"),
        limit: Optional[int] = Query(default=100, title="How many listings will be returned"),
        db: Session = Depends(get_db)
) -> Any:
    """
    Get all listings. Result can be filtered via skip and limit query parameters
    """
    results = listingRepo.read_all(db=db, skip=skip, limit=limit)
    if not results:
        return JSONResponse(
            status_code=404, content={"message": "No listing found"}
        )
    else:
        return results


@router.post("/", status_code=201, response_model=ListingSchema)
async def create_listing(
        *, data: ListingCreateSchema, db: Session = Depends(get_db)
) -> Any:
    """
    Create new listing
    """
    listing = listingRepo.create(db=db, obj_in=data)
    return listing


@router.put("/", status_code=201, response_model=ListingSchema, responses={404: {"model": Message}})
async def update_listing(
        *, data: ListingUpdateSchema, db: Session = Depends(get_db)
) -> Any:
    """
    Update listing. Existing listing will be matched through id
    """
    existing_listing = listingRepo.read(db=db, id=data.id)
    if not existing_listing:
        return JSONResponse(
            status_code=404, content={"message": f"Listing with ID {data.id} not found"}
        )
    else:
        listing = listingRepo.update(db=db, db_obj=existing_listing, obj_in=data)
        return listing


@router.delete("/{id}", status_code=200, response_model=ListingSchema, responses={404: {"model": Message}})
async def delete_listing(
        *,
        id: int = Path(title="ID of listing to be fetched"),
        db: Session = Depends(get_db)
) -> Any:
    """
    Deletes listing with given id
    """
    existing_listing = listingRepo.read(db=db, id=id)
    if not existing_listing:
        return JSONResponse(
            status_code=404, content={"message": f"Listing with ID {id} not found"}
        )
    else:
        deleted_listing = listingRepo.delete(db=db, id=id)
        return deleted_listing


@router.get("/search/{keyword}", status_code=200, response_model=Sequence[ListingSchema],
            responses={404: {"model": Message}})
async def search_listings(
        *,
        keyword: str = Path(title="Search keyword"),
        limit: Optional[int] = Query(default=100, title="How many records will be returned"),
        db: Session = Depends(get_db)
) -> Any:
    """
    Search for listings based address keyword
    """
    results = listingRepo.search(db=db, keyword=keyword, limit=limit)
    if not results:
        return JSONResponse(
            status_code=404, content={"message": "No listing found"}
        )
    return results
