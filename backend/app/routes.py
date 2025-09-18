from fastapi import APIRouter, HTTPException
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.services import generate_image_from_text
import uuid
import time
from datetime import datetime

router = APIRouter()

@router.post("/api/v1/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    start = time.time()
    try:
        image_b64 = await generate_image_from_text(req.input_text)
        elapsed = int((time.time() - start) * 1000)
        return AnalyzeResponse(
            id=str(uuid.uuid4()),
            task=req.task,
            engine="external:hf-stable-diffusion",
            result={"image_base64": image_b64},
            elapsed_ms=elapsed,
            received_at=datetime.utcnow().isoformat(),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/v1/healthz")
def healthz():
    return {"status": "ok"}
