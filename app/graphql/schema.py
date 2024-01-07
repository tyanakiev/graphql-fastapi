from typing import List

import strawberry

from app.graphql.definitions import Headers, Lines, Buyers, Items, Markets, SalesRep, Resource
from strawberry.fastapi import GraphQLRouter
from app.routers.routers import get_headers, get_lines, get_buyers, get_items, get_markets, get_resource, get_salesrep


@strawberry.type
class Query:
    @strawberry.field(is_subscription=False)
    async def get_headers(self) -> List[Headers]:
        return await get_headers()

    @strawberry.field(is_subscription=False)
    async def get_lines(self) -> List[Lines]:
        return await get_lines()

    @strawberry.field(is_subscription=False)
    async def get_buyers(self) -> List[Buyers]:
        return await get_buyers()

    @strawberry.field(is_subscription=False)
    async def get_items(self) -> List[Items]:
        return await get_items()

    @strawberry.field(is_subscription=False)
    async def get_markets(self) -> List[Markets]:
        return await get_markets()

    @strawberry.field(is_subscription=False)
    async def get_resource(self) -> List[Resource]:
        return await get_resource()

    @strawberry.field(is_subscription=False)
    async def get_salesrep(self) -> List[SalesRep]:
        return await get_salesrep()

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

