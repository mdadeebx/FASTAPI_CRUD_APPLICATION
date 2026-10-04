from fastapi import FastAPI,Request
from starlette.testclient import TestClient

from database import engine, SessionLocal
import models

from routers import auth,todos,admin,users

from fastapi.templating import Jinja2Templates


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="Todoapp/templates")


@app.get("/")
def test(request: Request):
    return templates.TemplateResponse(request, "home.html", {"todos": todos})

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)

app.include_router(users.router)


client = TestClient(app)
@app.get("/healthcheck")
def health_check():
    return {'status':'Healthy'}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
