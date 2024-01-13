from typing import Optional

import strawberry


@strawberry.type
class Headers:
    header_id: int
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    buyers: Optional["Buyers"]
    sales_rep: Optional["SalesRep"]
    lines: Optional["Lines"]


@strawberry.input
class HeadersInput:
    header_id: int
    name: Optional[str]


@strawberry.input
class HeadersDelete:
    header_id: int


@strawberry.type
class Lines:
    line_id: int
    header_id: int
    name: Optional[str]
    market_id: int
    item_id: int
    creation_date: str
    markets: Optional["Markets"]
    items: Optional["Items"]


@strawberry.type
class Buyers:
    buyer_id: int
    name: Optional[str]


@strawberry.input
class BuyersInput:
    buyer_id: int
    name: Optional[str]


@strawberry.input
class BuyersDelete:
    buyer_id: int


@strawberry.type
class Items:
    item_id: int
    name: Optional[str]
    description: Optional[str]


@strawberry.type
class Markets:
    market_id: int
    name: Optional[str]
    location: Optional[str]


@strawberry.type
class Resource:
    resource_id: int
    name: Optional[str]


@strawberry.type
class SalesRep:
    sales_rep_id: int
    resource_id: int
    resource: Optional[Resource]
