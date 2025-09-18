from pydantic import BaseModel
from typing import Optional, Dict
import uuid
from datetime import datetime

class AnalyzeRequest(BaseModel):
    task: str = "text-to-image"
    input_text: str
    use_external: bool = True
    options: Optional[Dict] = None

class AnalyzeResponse(BaseModel):
    id: str
    task: str
    engine: str
    result: Dict
    elapsed_ms: int
    received_at: str
