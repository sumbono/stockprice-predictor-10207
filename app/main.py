from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import the webpage routers
from app.webpage.homepage import homepage_router

# import the api endpoint routers
from app.api.predict import predict_endpoint
from app.api.train import train_endpoint

# import other necessary modules on app-startup
from app.metadata import metadata
from app.workers import background_threads


app = FastAPI(
    title=metadata["title"],
    description=metadata["description"],
    version=metadata["version"],
    contact=metadata["contact"],
    openapi_tags=metadata["tags"]
)

app.include_router(homepage_router)
app.include_router(predict_endpoint)
app.include_router(train_endpoint)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
async def startup() -> None:
    print("background threads starting...")
    background_threads.start()
