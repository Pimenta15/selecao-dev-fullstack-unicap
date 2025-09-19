import { useState } from "react";
import PromptForm from "./components/PromptForm";
import ResultView from "./components/ResultView";
import { generateImage } from "./api";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [imageBase64, setImageBase64] = useState(null);

  const handleGenerate = async (prompt) => {
    setLoading(true);
    setError(null);
    setImageBase64(null);
    try {
      const result = await generateImage(prompt);
      setImageBase64(result.result.image_base64);
    } catch (err) {
      setError(err.toString());
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-lg mx-auto text-center">
      <h1 className="text-2xl font-bold mb-4">Text-to-Image Generator</h1>
      <PromptForm onSubmit={handleGenerate} />
      <ResultView loading={loading} error={error} imageBase64={imageBase64} />
    </div>
  );
}
