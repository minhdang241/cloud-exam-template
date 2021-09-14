import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings


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


# add your route here
@app.get("/")
def test():
    return "Backend is up"


@app.get("/add")
def add(a: int, b: int) -> int:
    return a + b


# @app.get_singer("/singers/{id}", response_class=HTMLResponse)
# def get_singers(request: Request, id: int, db_session: Session = Depends(get_db)):
# return templates.TemplateResponse("singer.html", {"request": request, "id": id})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
