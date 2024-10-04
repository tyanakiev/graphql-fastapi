from typing import List

import strawberry
import asyncio
from app.graphql.definitions import Headers, Lines, Buyers, Items, Markets, SalesRep, Resource, BuyersInput,\
    BuyersDelete, HeadersInput, HeadersDelete

from strawberry.fastapi import GraphQLRouter
from app.routers.routers import get_headers, get_lines, get_buyers, get_items, get_markets, get_resource,\
    get_salesrep, insert_buyer, update_buyer, delete_buyer, insert_header, update_header, delete_header


async def sleep_for_2_seconds(name: str, time: int) -> str:
    await asyncio.sleep(time)
    print(f"{name} has finished sleeping")
    return f"{name} has finished sleeping"

@strawberry.type
class Query:
    @strawberry.field
    async def get_headers(self) -> List[Headers]:
        return await get_headers()

    @strawberry.field
    async def get_lines(self) -> List[Lines]:
        return await get_lines()

    @strawberry.field
    async def get_buyers(self) -> List[Buyers]:
        return await get_buyers()

    @strawberry.field
    async def get_items(self) -> List[Items]:
        return await get_items()

    @strawberry.field
    async def get_markets(self) -> List[Markets]:
        return await get_markets()

    @strawberry.field
    async def get_resource(self) -> List[Resource]:
        return await get_resource()

    @strawberry.field
    async def get_salesrep(self) -> List[SalesRep]:
        return await get_salesrep()

    @strawberry.field
    async def get_salesrep(self) -> List[SalesRep]:
        return await get_salesrep()

    @strawberry.field
    async def test_sleep_1(self) -> str:
        print("Starting sleep 1")
        return await sleep_for_2_seconds("Function 1", 2)

    @strawberry.field
    async def test_sleep_2(self) -> str:
        print("Starting sleep 2")
        return await sleep_for_2_seconds("Function 2", 4)

    @strawberry.field
    async def test_sleep_3(self) -> str:
        print("Starting sleep 3")
        return await sleep_for_2_seconds("Function 3", 6)

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

