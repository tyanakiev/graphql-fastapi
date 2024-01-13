from typing import List

import strawberry

from app.graphql.definitions import Headers, Lines, Buyers, Items, Markets, SalesRep, Resource, BuyersInput,\
    BuyersDelete, HeadersInput, HeadersDelete

from strawberry.fastapi import GraphQLRouter
from app.routers.routers import get_headers, get_lines, get_buyers, get_items, get_markets, get_resource,\
    get_salesrep, insert_buyer, update_buyer, delete_buyer, insert_header, update_header, delete_header


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


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_buyer(self, buyer: BuyersInput) -> Buyers:
        return await insert_buyer(buyer)

    @strawberry.mutation
    async def update_buyer(self, buyer: BuyersInput) -> Buyers:
        return await update_buyer(buyer)

    @strawberry.mutation
    async def delete_buyer(self, buyer: BuyersDelete) -> bool:
        return await delete_buyer(buyer_id=buyer.buyer_id)

    @strawberry.mutation
    async def create_header(self, header: HeadersInput) -> Headers:
        return await insert_header(header)

    @strawberry.mutation
    async def update_header(self, header: HeadersInput) -> Headers:
        return await update_header(header)

    @strawberry.mutation
    async def delete_header(self, header: HeadersDelete) -> bool:
        return await delete_header(header_id=header.header_id)


schema = strawberry.Schema(query=Query, mutation=Mutation)

# schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

