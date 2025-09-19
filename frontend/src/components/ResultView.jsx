export default function ResultView({ loading, error, imageBase64 }) {
    if (loading) return <p>⏳ Gerando imagem...</p>;
    if (error) return <p className="text-red-600">❌ {error}</p>;
    if (imageBase64)
      return (
        <div className="mt-4">
          <img
            src={`data:image/png;base64,${imageBase64}`}
            alt="Gerado pela IA"
            className="border rounded shadow-md max-w-full"
          />
        </div>
      );
    return null;
  }
  