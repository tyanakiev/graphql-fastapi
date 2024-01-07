from pydantic import BaseModel
from typing import Optional, List


class HeadersModel(BaseModel):
    header_id: Optional[int]
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    # Not having = None for the reletionship would result in circular import error.
    buyers: Optional["BuyersModel"] = None
    sales_rep: Optional["SalesRepModel"] = None
    lines: Optional["LinesModel"] = None


class LinesModel(BaseModel):
    line_id: Optional[int]
    header_id: Optional[int]
    name: Optional[str]
    market_id: Optional[int]
    item_id: Optional[int]
    creation_date: Optional[str]
    header: Optional["HeadersModel"] = None
    # markets: Optional["MarketsModel"] = None

    # Reflect the relationships
    # header: Optional["HeadersModel"]
    # market: Optional["MarketsModel"]
    # item: Optional["ItemsModel"]


class BuyersModel(BaseModel):
    buyer_id: Optional[int]
    name: Optional[str]

    # Reflect the relationships
    header: Optional["HeadersModel"] = None


class ItemsModel(BaseModel):
    item_id: Optional[int]
    name: Optional[str]
    description: Optional[str]

    # Reflect the relationships
    # lines: Optional[List["LinesModel"]]


class MarketsModel(BaseModel):
    market_id: Optional[int]
    name: Optional[str]
    location: Optional[str]

    # Reflect the relationships
    # lines: Optional[List["LinesModel"]]


class ResourceModel(BaseModel):
    resource_id: Optional[int]
    name: Optional[str]

    # Reflect the relationships
    # sales_rep: Optional["SalesRepModel"]


class SalesRepModel(BaseModel):
    sales_rep_id: Optional[int]
    resource_id: Optional[int]

    # Reflect the relationships
    header: Optional["HeadersModel"] = None
