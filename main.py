import uvicorn
from fastapi import FastAPI, Request, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config import settings
from utils import get_db
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from crud import crud_singer

from db.postgres import models
from db.postgres.setup_postgres import engine
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

models.Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        description="""
        FASTAPI template
        """,
    )

    application.mount("/static", StaticFiles(directory="static"), name="static")
    # add config or middleware here
    return application


templates = Jinja2Templates(directory="templates")

app = get_application()


# Return Homepage
@app.get("/", response_class=HTMLResponse)
def get_singers(request: Request, db_session: Session = Depends(get_db)):
    singers = crud_singer.singer.get(db_session)
    return templates.TemplateResponse("page/index.html", {"request": request, "singers": singers})


# Return Edit form
@app.get("/singers/{id}/edit", response_class=HTMLResponse)
def get_edit_singer_form(request: Request, id: int, db_session: Session = Depends(get_db)):
    singers = crud_singer.singer.get(db_session)
    singer_obj = crud_singer.singer.get_by_id(db_session, id=id)
    return templates.TemplateResponse("page/index.html", {"request": request, "singers": singers, "singer": singer_obj})


# Edit object and redirect to homepage
@app.post("/singers/{id}/edit", response_class=HTMLResponse)
def edit_singer(id: int,
                name: str = Form(...), nick_name: str = Form(...), # EDIT FIELD HERE ###
                db_session: Session = Depends(get_db)):
    update_obj = crud_singer.SingerCreate(
        name=name,
        nick_name=nick_name,
        birthday="Na",
        address="Na",
        songs=[]
    )
    db_obj = crud_singer.singer.get_by_id(db_session, id=id)
    crud_singer.singer.update(db_session, db_obj=db_obj, obj_in=update_obj)
    return RedirectResponse("/", status_code=HTTP_302_FOUND)


# Create object and redirect to homepage
@app.post("/", response_class=HTMLResponse)
def post_singer(name: str = Form(...), nick_name: str = Form(...), # EDIT FIELD HERE ###
                db_session: Session = Depends(get_db)):

    create_obj = crud_singer.SingerCreate(
        name=name,
        nick_name=nick_name,
        birthday="Na",
        address="Na",
        songs=[]
    )
    crud_singer.singer.create(db_session, obj_in=create_obj)

    return RedirectResponse("/", status_code=HTTP_302_FOUND)


# Delete object and redirect to homepage
@app.post("/singers/{id}/delete", response_class=HTMLResponse)
def post_singer(id: int, db_session: Session = Depends(get_db)):

    crud_singer.singer.remove(db_session, id=id)

    return RedirectResponse("/", status_code=HTTP_302_FOUND)


@app.get("/add")
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
