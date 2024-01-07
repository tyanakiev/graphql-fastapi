
import sqlalchemy
from fastapi import FastAPI
from app.database.database import engine, Base
from app.graphql.schema import graphql_app
from app.routers import routers

Base.metadata.create_all(bind=engine)

# metadata = sqlalchemy.MetaData()
# metadata.create_all(database.engine)
app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")
app.include_router(routers.router)


@app.on_event("startup")
async def startup():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    # Additional initialization logic can be added here
    print("Database connected on startup")


@app.on_event("shutdown")
async def shutdown():
    engine.dispose()
    print("Database disconnected on shutdown")
