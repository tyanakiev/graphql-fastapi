# FastAPI, SQLAlchemy, and Strawberry GraphQL POC

This project serves as a demonstration of the seamless integration between FastAPI, SQLAlchemy, and Strawberry GraphQL, utilizing an SQLite3 database. It aims to showcase the synergy and capabilities of these technologies when combined.

## Key Features

- **FastAPI Integration:** Utilizes FastAPI, a modern, fast, web framework for building APIs with Python 3.7+.

- **SQLAlchemy Database:** Leverages SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library.

- **Strawberry GraphQL:** Implements Strawberry, a GraphQL library for Python with a code-first approach.

- **SQLite3 Database:** Utilizes SQLite3 as the backend database for ease of setup and portability.

## Getting Started

Follow these steps to download, install requirements, and start the FastAPI server:

### Prerequisites

- Ensure you have Python 3.7 or higher installed.

### Download and Install

1. Clone the repository:

   ```git clone https://github.com/your-username/your-fastapi-project.git```

2. Change into the project directory:

   ```cd graphql-fastapi```

3. Create and activate a virtual environment:

   ```python -m venv venv```
   ```source venv/bin/activate   # On Windows, use `venv\Scripts\activate```

4. Install dependencies:

   ```pip install -r requirements.txt```

### Start FastAPI Server

Run the FastAPI server with the following command:

   ```uvicorn main:app --reload```

Visit http://127.0.0.1:8000/docs in your browser to access the Swagger documentation and explore available API endpoints.

## GraphQL API

### Access the GraphQL Playground

Visit http://127.0.0.1:8000/graphql in your browser to access the GraphQL Playground.

### Examples of GraphQL Queries

#### Get Resource Data

```graphql
query MyQuery {
  getHeaders {
    active
    buyerId
    headerId
    name
    salesRepId
    lines {
      creationDate
      headerId
      itemId
      lineId
      marketId
      name
      items {
        description
        itemId
        name
      }
      markets {
        location
        marketId
        name
      }
    }
    salesRep {
      resourceId
      salesRepId
      resource {
        name
        resourceId
      }
    }
    buyers {
      buyerId
      name
    }
  }
}
```
### Resposnse:

```
{
  "data": {
    "getHeaders": [
      {
        "active": "Y",
        "buyerId": 1003,
        "headerId": 1,
        "name": "Header Name 1",
        "salesRepId": 102,
        "lines": {
          "creationDate": "2023-01-01",
          "headerId": 1,
          "itemId": 701,
          "lineId": 55001,
          "marketId": 2201,
          "name": "Line Name 1",
          "items": {
            "description": "gold",
            "itemId": 701,
            "name": "gold"
          },
          "markets": {
            "location": "Europe",
            "marketId": 2201,
            "name": "NotSo Wet Market"
          }
        },
        "salesRep": {
          "resourceId": 12,
          "salesRepId": 102,
          "resource": {
            "name": "Jaba Maba",
            "resourceId": 12
          }
        },
        "buyers": {
          "buyerId": 1003,
          "name": "Simon Sims"
        }
      },
      {
        "active": "Y",
        "buyerId": 1002,
        "headerId": 2,
        "name": "Header Name 2",
        "salesRepId": 105,
        "lines": {
          "creationDate": "2022-01-05",
          "headerId": 2,
          "itemId": 701,
          "lineId": 55003,
          "marketId": 2203,
          "name": "Line Name 3",
          "items": {
            "description": "gold",
            "itemId": 701,
            "name": "gold"
          },
          "markets": {
            "location": "Africa",
            "marketId": 2203,
            "name": "Rainy Days Market"
          }
        },
        "salesRep": {
          "resourceId": 15,
          "salesRepId": 105,
          "resource": {
            "name": "Viper Song",
            "resourceId": 15
          }
        },
        "buyers": {
          "buyerId": 1002,
          "name": "Bobby DropTable"
        }
      },
      {
        "active": "N",
        "buyerId": 1005,
        "headerId": 3,
        "name": "Header Name 3",
        "salesRepId": 101,
        "lines": {
          "creationDate": "2024-01-01",
          "headerId": 3,
          "itemId": 704,
          "lineId": 55004,
          "marketId": 2204,
          "name": "Line Name 4",
          "items": {
            "description": "dirt",
            "itemId": 704,
            "name": "dirt"
          },
          "markets": {
            "location": "North America",
            "marketId": 2204,
            "name": "PewPew market"
          }
        },
        "salesRep": {
          "resourceId": 11,
          "salesRepId": 101,
          "resource": {
            "name": "Jim Salibana",
            "resourceId": 11
          }
        },
        "buyers": {
          "buyerId": 1005,
          "name": "Tom Riddle"
        }
      }
    ]
  }
}
```

![image](https://github.com/tyanakiev/graphql-fastapi/assets/5628399/9602e42c-f021-4af1-bad8-5105f38723d4)
