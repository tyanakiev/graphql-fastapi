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

   ```cd your-fastapi-project```

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
  getResource {
    name
    resourceId
  }
}
```
### Resposnse:

```
{
  "data": {
    "getResource": [
      {
        "name": "Jim Salibana",
        "resourceId": 11
      },
      {
        "name": "Jaba Maba",
        "resourceId": 12
      },
      {
        "name": "Jim Harpy",
        "resourceId": 13
      },
      {
        "name": "Soltan Han",
        "resourceId": 14
      },
      {
        "name": "Viper Song",
        "resourceId": 15
      },
      {
        "name": "Kilrog HowtoexitVIM",
        "resourceId": 16
      }
    ]
  }
}
```
