# FastAPI and Docker
*This guide will lead you through the usage of FastAPI, Tortoise ORM, Docker, and PyTest*


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

- **_project/app/main.py_** - Starts the application, in our case we use uvicorn
- **_project/app/config.py_** - Application configurations, environment variables, etc.
- **_project/app/db.py_** - Sets up database and initializing the connection with the app
- **_project/db/create.sql_** - SQL scripts that creates our databases, CRUD operations are handled elsewhere
- **_project/tests/conftest.py_** - Configuration for our PyTests
- **_project/app/Dockerfile_** - Docker will spin up a slim-buster Docker image with Python 3.9.2, this creates the web app container
- **_project/db/Dockerfile_** - Docker will spin up a postgres container, create a database, and serve as our database container
- **_docker-compose.yml_** - Builds and configures our web and webdb containers, while triggering the Dockerfiles within the `project` directory


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
docker compose up -d
```
3. Explore the URL of the API: http://localhost:8004/

### Useful Commands

---
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