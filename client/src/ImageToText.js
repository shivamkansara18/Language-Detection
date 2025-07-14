import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

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
    <div className="image-to-text-container">
      <h2 className="page-title">Image to Text & Language Detection</h2>
      <form onSubmit={handleSubmit} className="image-form">
        <input type="file" accept="image/*" onChange={handleImageUpload} className="file-input" />
        <button type="submit" className="submit-button">Extract Text</button>
      </form>
      {extractedText && (
        <div className="result-container">
          <h3 className="detected-language">Detected Language: {detectedLang}</h3>
          <p><strong>Extracted Text:</strong> {extractedText}</p>
        </div>
      )}
    </div>
  );
};

export default ImageToText;
