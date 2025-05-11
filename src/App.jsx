import { useState } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    if (!prompt) return alert('Enter a prompt');
    setLoading(true);
    setImage(null);
    try {
      const response = await axios.post(
        'https://navadeep-j-sample-storyboard.hf.space/generate',
        { prompt }
      );
      setImage("data:image/png;base64," + response.data.image);
    } catch (error) {
      alert('Failed to generate image.');
      console.error(error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-6 text-center">Storyboard Image Generator</h1>
      <input
        type="text"
        placeholder="Enter your prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="w-full max-w-xl border rounded p-3 mb-4 shadow"
      />
      <button
        onClick={generateImage}
        disabled={loading}
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? 'Generating...' : 'Generate Image'}
      </button>
      {image && (
        <img
          src={image}
          alt="Generated AI"
          className="mt-6 rounded-lg shadow-lg max-w-full h-auto"
        />
      )}
    </div>
  );
}

export default App;
