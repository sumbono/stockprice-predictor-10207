from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import the webpage routers
from app.webpage.homepage import homepage_router

# import the api endpoint routers
from app.api.predict import predict_endpoint
from app.api.predict_plotter import predict_plotter_endpoint
from app.api.train import train_endpoint

# import other necessary modules on app-startup
from app.api.metadata import metadata


app = FastAPI(
    title=metadata["title"],
    description=metadata["description"],
    version=metadata["version"],
    contact=metadata["contact"],
    openapi_tags=metadata["tags"]
)

app.include_router(predict_endpoint)
app.include_router(predict_plotter_endpoint)
app.include_router(train_endpoint)

app.include_router(homepage_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
