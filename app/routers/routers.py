from typing import List

from app.models.models import Headers, Lines, Buyers, Items, Markets, Resource, SalesRep
from app.models.schema import HeadersModel, LinesModel, BuyersModel, ItemsModel, MarketsModel, ResourceModel, SalesRepModel
from fastapi import APIRouter
from app.database.database import SessionLocal

router = APIRouter()
db = SessionLocal()


@router.get("/headers", response_model=List[HeadersModel], tags=["headers"])
async def get_headers():
    headers = db.query(Headers).all()
    return headers


@router.get("/lines", response_model=List[LinesModel], tags=["lines"])
async def get_lines():
    buyers = db.query(Lines).all()
    return buyers


@router.get("/buyers", response_model=List[BuyersModel], tags=["buyers"])
async def get_buyers():
    buyers = db.query(Buyers).all()
    return buyers


@router.get("/items", response_model=List[ItemsModel], tags=["items"])
async def get_items():
    items = db.query(Items).all()
    return items


@router.get("/markets", response_model=List[MarketsModel], tags=["markets"])
async def get_markets():
    markets = db.query(Markets).all()
    return markets


@router.get("/resource", response_model=List[ResourceModel], tags=["resource"])
async def get_resource():
    resource = db.query(Resource).all()
    return resource


@router.get("/salesrep", response_model=List[SalesRepModel], tags=["salesrep"])
async def get_salesrep():
    salesrep = db.query(SalesRep).all()
    return salesrep
