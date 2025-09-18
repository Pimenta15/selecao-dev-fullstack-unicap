import os
import time
import base64
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY") or os.getenv("HF_TOKEN")

if not HF_API_KEY:
    raise ValueError("⚠️ Defina HF_API_KEY ou HF_TOKEN no .env")

# Cria o cliente de inferência
client = InferenceClient(api_key=HF_API_KEY)

async def generate_image_from_text(prompt: str) -> str:
    """
    Usa Hugging Face InferenceClient (ex: Qwen/Qwen-Image) para gerar imagem a partir de texto.
    Retorna a imagem em Base64.
    """
    model = "Qwen/Qwen-Image"

    start = time.time()
    image = client.text_to_image(prompt, model=model)  # retorna PIL.Image

    # Converte para Base64
    from io import BytesIO
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    return image_b64
