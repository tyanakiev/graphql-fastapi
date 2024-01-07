from dataclasses import dataclass
from typing import Optional, List


@dataclass
class HeadersModel:
    header_id: Optional[int]
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    # Not having = None for the reletionship would result in circular import error.
    buyers: Optional["BuyersModel"] = None
    sales_rep: Optional["SalesRepModel"] = None
    lines: Optional["LinesModel"] = None


@dataclass
class LinesModel:
    line_id: Optional[int]
    header_id: Optional[int]
    name: Optional[str]
    market_id: Optional[int]
    item_id: Optional[int]
    creation_date: Optional[str]
    header: Optional["HeadersModel"] = None
    market: Optional["MarketsModel"] = None


@dataclass
class BuyersModel:
    buyer_id: Optional[int]
    name: Optional[str]

    # Reflect the relationships
    header: Optional["HeadersModel"] = None


@dataclass
class ItemsModel:
    item_id: Optional[int]
    name: Optional[str]
    description: Optional[str]

    # Reflect the relationships
    # lines: Optional[List["LinesModel"]]


@dataclass
class MarketsModel:
    market_id: Optional[int]
    name: Optional[str]
    location: Optional[str]
    lines: Optional[List["LinesModel"]]


@dataclass
class ResourceModel:
    resource_id: Optional[int]
    name: Optional[str]

    # Reflect the relationships
    sales_rep: Optional["SalesRepModel"]= None


@dataclass
class SalesRepModel:
    sales_rep_id: Optional[int]
    resource_id: Optional[int]

    # Reflect the relationships
    header: Optional["HeadersModel"] = None
    resource: Optional["ResourceModel"] = None
