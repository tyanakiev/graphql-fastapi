from pydantic import BaseModel
from typing import Optional


class HeadersModel(BaseModel):
    header_id: Optional[int]
    name: Optional[str]


class LinesModel(BaseModel):
    line_id: Optional[int]
    header_id: Optional[int]
    name: Optional[str]
    market: Optional[int]
    item: Optional[int]
    creation_date: Optional[str]


class BuyersModel(BaseModel):
    buyer_id: Optional[int]
    name: Optional[str]


class ItemsModel(BaseModel):
    item_id: Optional[int]
    name: Optional[str]
    description: Optional[str]


class MarketsModel(BaseModel):
    market_id: Optional[int]
    name: Optional[str]
    location: Optional[str]


class ResourceModel(BaseModel):
    resource_id: Optional[int]
    name: Optional[str]


class SalesRepModel(BaseModel):
    sales_rep_id: Optional[int]
    resource_id: Optional[int]