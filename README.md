
# FASTAPI_CRUD_APPLICATION


CRUD Application API is built with ""FASTAPI"",with RESTful API routes , server-side rendered pages, and secure user authentication 




## Features

- RESTful API routers built with FastAPI
- Server-side rendering with Jinja2 Templates
- User registration and login with JWT-based authentication and authorization
- Password database models with SQLAlchemy ORM
-Version-controlled schema migrations with Alembic




## Tech Stack

Python,FastAPI,SQLAlchemy,Alembic,Jinja2,JWT,HTML/CSS


## Installation

1. Clone the repo

```bash
  git clone https://github.com/mdadeebx/FASTAPI_CRUD_APPLICATION.git
  cd FASTAPI_CRUD_APPLICATION

```
2. Create a virtual environment and install dependencies 
```bash
python -m venv venv
source venv/bin/activate (Windows:venv\Scripts\activate)
pip install -r requirements.txt
```
3. Start the app
```bash
uvicorn main:app --reload
```
4. Open the URL use API at /docs


## Lessons Learned

- Structure a FastAPI project with routers and dependency injection
- Implementing JWT authentication and password hashing
- Designing relational schemas and managing migrations with Alembic


