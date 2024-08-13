from fastapi import FastAPI

from app.api.v1 import tts_router, chatbot_router, etc_router


app = FastAPI()

# Including API routers
app.include_router(tts_router.router)
app.include_router(chatbot_router.router)
app.include_router(etc_router.router)
