from fastapi import FastAPI
from views.views import router as views_router

app = FastAPI()
app.include_router(
    views_router,
    prefix="/ping",
    tags=["ping"]
)


@app.get("/")
def root():
    return {"message": "Hello world!!!"}


@app.get("/hello/")
def user(name="Guest"):
    return {"message": f"Hello {name}!!!"}
