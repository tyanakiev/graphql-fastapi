from typing import List

from app.models.models import Headers, Lines, Buyers, Items, Markets, Resource, SalesRep
from app.models.schema import HeadersModel, LinesModel, BuyersModel, ItemsModel, MarketsModel, ResourceModel, SalesRepModel
from fastapi import APIRouter
from app.database.database import SessionLocal

router = APIRouter()
db = SessionLocal()


@router.get("/headers", response_model=None, tags=["headers"])
async def get_headers() -> List[HeadersModel]:
    headers = db.query(Headers).all()
    return headers


@router.get("/lines", response_model=None, tags=["lines"])
async def get_lines()->List[LinesModel]:
    buyers = db.query(Lines).all()
    return buyers


@router.get("/buyers", response_model=None, tags=["buyers"])
async def get_buyers() ->List[BuyersModel]:
    buyers = db.query(Buyers).all()
    return buyers


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
