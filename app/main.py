from fastapi import FastAPI

from app.api.v1 import tts_router


app = FastAPI()

# Including API routers
app.include_router(tts_router.router)
