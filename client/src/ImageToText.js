// components/ImageToText.js
import React, { useState } from 'react';
import axios from 'axios';

const ImageToText = () => {
  const [image, setImage] = useState(null);
  const [extractedText, setExtractedText] = useState('');
  const [detectedLang, setDetectedLang] = useState('');

  const handleImageUpload = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) return;

    const formData = new FormData();
    formData.append('image', image);

    try {
      const res = await axios.post('http://localhost:8000/image-to-text', formData);
      setExtractedText(res.data.text);
      setDetectedLang(res.data.detectedLang);
    } catch (err) {
      console.error(err);
      alert('Error processing image');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Image to Text & Language Detection</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleImageUpload} />
        <button type="submit">Extract Text</button>
      </form>
      {extractedText && (
        <div style={{ marginTop: '1rem' }}>
          <h3>Detected Language: {detectedLang}</h3>
          <p><strong>Extracted Text:</strong> {extractedText}</p>
        </div>
      )}
    </div>
  );
};

export default ImageToText;
