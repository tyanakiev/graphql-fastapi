from typing import List
from fastapi import HTTPException
from app.models.models import Headers, Lines, Buyers, Items, Markets, Resource, SalesRep
from app.models.schema import HeadersModel, LinesModel, BuyersModel, ItemsModel, MarketsModel, ResourceModel, SalesRepModel
from fastapi import APIRouter
from app.database.database import SessionLocal
from fastapi.encoders import jsonable_encoder

router = APIRouter()
db = SessionLocal()


@router.get("/headers", response_model=None, tags=["headers"])
async def get_headers() -> List[HeadersModel]:
    headers = db.query(Headers).all()
    return headers


@router.post("/add-headers/", tags=["headers"])
async def insert_header(header: HeadersModel):
    new_header = Headers(
        header_id=header.header_id,
        name=header.name,
        sales_rep_id=header.sales_rep_id,
        buyer_id=header.buyer_id,
        active=header.active
    )

    db.add(new_header)
    db.commit()
    db.refresh(new_header)
    return new_header


@router.put("/update-headers/", tags=["headers"])
async def update_header(updated_header: HeadersModel):
    print(updated_header)
    existing_header = db.query(Headers).filter(Headers.header_id == updated_header.header_id).first()

    if existing_header:
        # Update the attributes of the existing header
        for field, value in jsonable_encoder(updated_header).items():
            print(field, value)
            if value:
                setattr(existing_header, field, value)

        db.commit()
        db.refresh(existing_header)
        return existing_header

    return {"message": "Header not found"}


@router.delete("/delete-headers/{header_id}", tags=["headers"])
async def delete_header(header_id: int):
    existing_header = db.query(Headers).filter(Headers.header_id == header_id).first()

    if existing_header:
        db.delete(existing_header)
        db.commit()
        return True

    return False


@router.get("/lines", response_model=None, tags=["lines"])
async def get_lines()->List[LinesModel]:
    buyers = db.query(Lines).all()
    return buyers


@router.get("/buyers", response_model=None, tags=["buyers"])
async def get_buyers() ->List[BuyersModel]:
    buyers = db.query(Buyers).all()
    return buyers


@router.post("/add-buyers/", tags=["buyers"])
async def insert_buyer(buyer: BuyersModel):
    new_buyer = Buyers(
        buyer_id=buyer.buyer_id,
        name=buyer.name,
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return buyer


@router.put("/update-buyer/", tags=["buyers"])
async def update_buyer(updated_buyer: BuyersModel):
    existing_buyer = db.query(Buyers).filter(Buyers.buyer_id == updated_buyer.buyer_id).first()

    if existing_buyer:
        # Update the attributes of the existing buyer excluding 'buyer_id'
        update_item_encoded = jsonable_encoder(updated_buyer)
        for field, value in update_item_encoded.items():
            if field != "buyer_id":
                setattr(existing_buyer, field, value)

        db.commit()
        db.refresh(existing_buyer)
        return existing_buyer

    return {"message": "Buyer not found"}


@router.delete("/delete-buyer/{buyer_id}", tags=["buyers"])
async def delete_buyer(buyer_id: int):
    existing_buyer = db.query(Buyers).filter(Buyers.buyer_id == buyer_id).first()

    if existing_buyer:
        db.delete(existing_buyer)
        db.commit()
        return True

    return False


@router.get("/items", response_model=None, tags=["items"])
async def get_items()->List[ItemsModel]:
    items = db.query(Items).all()
    return items


@router.get("/markets", response_model=None, tags=["markets"])
async def get_markets() -> List[MarketsModel]:
    markets = db.query(Markets).all()
    return markets


@router.get("/resource", response_model=None, tags=["resource"])
async def get_resource() -> List[ResourceModel]:
    resource = db.query(Resource).all()
    return resource


@router.get("/salesrep", response_model=None, tags=["salesrep"])
async def get_salesrep()->List[SalesRepModel]:
    salesrep = db.query(SalesRep).all()
    return salesrep
