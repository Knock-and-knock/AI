from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.service.melo_tts_service import convert_text_to_speech
from app.service.openai_tts_service import convert_text_to_speech_openai

router = APIRouter(
    prefix="/api/v1",
    tags=["Auth"]
)

@router.get("/melo/tts")
async def melo_tts(contents: str):
    try:
        buffer = convert_text_to_speech(contents)
        return StreamingResponse(buffer, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/openai/tts")
async def openai_tts(contents: str):
    try:
        buffer = convert_text_to_speech_openai(contents)
        return StreamingResponse(buffer, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
