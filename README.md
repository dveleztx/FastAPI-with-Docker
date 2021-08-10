# FastAPI and Docker
*This guide will lead you through the usage of FastAPI, Tortoise ORM, Docker, and PyTest*

## CI-CD

![Continuous Integration and Delivery](https://github.com/dveleztx/FastAPI-with-Docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

## Structure of Application

```
.
├── docker-compose.yml
├── project
│   ├── app
│   │   ├── api
│   │   │   ├── crud.py
│   │   │   ├── __init__.py
│   │   │   ├── ping.py
│   │   │   └── summaries.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── models
│   │       ├── __init__.py
│   │       ├── pydantic.py
│   │       └── tortoise.py
│   ├── db
│   │   ├── create.sql
│   │   └── Dockerfile
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── requirements.txt
│   └── tests
│       ├── conftest.py
│       ├── __init__.py
│       ├── test_ping.py
│       └── test_summaries.py
└── README.md
```

### Important Files

- [project/app/main.py](./project/app/main.py) - Starts the application, in our case we use uvicorn
- [project/app/config.py](./project/app/config.py) - Application configurations, environment variables, etc.
- [project/app/db.py](./project/app/db.py) - Sets up database and initializing the connection with the app
- [project/db/create.sql](./project/db/create.sql) - SQL scripts that creates our databases, CRUD operations are handled elsewhere
- [project/tests/conftest.py](./project/tests/conftest.py) - Configuration for our PyTests
- [project/app/Dockerfile](./project/app/Dockerfile) - Docker will spin up a slim-buster Docker image with Python 3.9.2, this creates the web app container
- [project/db/Dockerfile](./project/db/Dockerfile) - Docker will spin up a postgres container, create a database, and serve as our database container
- [docker-compose.yml](./docker-compose.yml) - Builds and configures our web and webdb containers, while triggering the Dockerfiles within the `project` directory


### Things to know

- Logging has been configured for `main.py`, `db.py`, `config.py` that is pointing to our web service: *uvicorn*
- To run the app locally, from the `project` directory, run `uvicorn app.main:app --reload`
  - The `--reload` argument updates the page with any changes you make on the project files
  - **NOTE**: The databases are going to have to be created for the app to work locally, and connection strings are going to need to be written


## Usage

Docker is the intended way to run this application. To install it, follow these [docs](https://docs.docker.com/get-docker/).

### Setup Instructions

1. We first need to build our docker image
```bash
docker-compose build
```
2. Next, once the build is done, kick off the container in detached mode (runs in the background):
```bash
docker-compose up -d
```
3. Now, generate the database schemas:
```bash
docker-compose exec web python app/db.py
```   
4. Explore the URL of the API: http://localhost:8004/
5. To explore the SWAGGER-like API Docs, explore to: http://localhost:8004/docs

---

### API Endpoints

| Endpoint       | HTTP Method | Result                         |
|:---------------|:-----------:|:-------------------------------|
| /ping          | GET         | Get environment configs + Pong!|
| /summaries     | GET         | Get all summaries              |
| /summaries/:id | GET         | Get a single summary           |
| /summaries     | POST        | Add a summary                  |
| /summaries/:id | PUT         | Update a summary               |
| /summaries/:id | DELETE      | Delete a summary               |

---

### Testing Endpoints using PyTest

Tests are stored in **project/tests** directory. There are two scripts, one for testing the *ping* endpoint, and one for the *summaries* endpoints.

**NOTE**: In order to perform PyTests, the webapp must be running in a docker container. Also, the **conftest.py** file should not be changed, as it is a recognized template name for looking for pytest configurations.

To run the pytests, run the following command:

```bash
docker-compose exec web python -m pytest
```

To generate a report with PyTest, run the following command:

```bash
docker-compose exec web python -m pytest --cov="."
```

---

### Useful Commands

To re-build any new changes to application:
```bash
docker-compose up -d --build
```
---
Check logs on docker containers (call by name):
```bash
docker-compose logs web
docker-compose logs web-db
```
---
Access PostgreSQL Database:
```bash
docker-compose exec web-db psql -U postgres
```
---
To POST a url into the summaries database, use [httpie](https://httpie.io/):
```bash
http --json POST http://localhost:8004/summaries/ url=http://example.com
```

