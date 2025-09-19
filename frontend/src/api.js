import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/v1";

export async function generateImage(prompt) {
  try {
    const response = await axios.post(`${API_URL}/analyze`, {
      task: "text-to-image",
      input_text: prompt,
      use_external: true,
    });
    return response.data;
  } catch (err) {
    throw err.response?.data?.detail || "Erro ao gerar imagem";
  }
}
