from dataclasses import dataclass
from typing import Optional, List


@dataclass
class BuyersModel:
    buyer_id: int
    name: Optional[str]


@dataclass
class ItemsModel:
    item_id: int
    name: Optional[str]
    description: Optional[str]


@dataclass
class MarketsModel:
    market_id: int
    name: Optional[str]
    location: Optional[str]


@dataclass
class ResourceModel:
    resource_id: int
    name: Optional[str]


@dataclass
class SalesRepModel:
    sales_rep_id: int
    resource_id: Optional[int]

    # Reflect the relationships
    resource: Optional[ResourceModel] = None


@dataclass
class LinesModel:
    line_id: int
    header_id: Optional[int]
    name: Optional[str]
    market_id: Optional[int]
    item_id: Optional[int]
    creation_date: Optional[str]
    market: Optional[MarketsModel] = None


@dataclass
class HeadersModel:
    header_id: int
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    buyers: Optional[BuyersModel] = None
    sales_rep: Optional[SalesRepModel] = None
    lines: Optional[LinesModel] = None



