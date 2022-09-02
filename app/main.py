from app.endpoints import app
from app.workers import background_threads

@app.on_event("startup")
async def startup() -> None:
    print("background threads starting...")
    background_threads.start()
