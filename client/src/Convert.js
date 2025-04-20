import React, { useState } from 'react';
import axios from 'axios';

const languages = [
  'English', 'Malayalam', 'Hindi', 'Tamil', 'Kannada', 'French', 'Spanish',
  'Portuguese', 'Italian', 'Russian', 'Sweedish', 'Dutch', 'Arabic', 
  'Turkish', 'German', 'Danish', 'Greek'
];

const Convert = () => {
  const [text, setText] = useState('');
  const [targetLang, setTargetLang] = useState('English');
  const [detectedLang, setDetectedLang] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  const user = JSON.parse(localStorage.getItem('user'));

  const handleConvert = async () => {
    try {
      const res = await axios.post('http://localhost:5000/api/detection/analyze', {
        text,
        targetLang,
        userId: user._id
      });

      // Ensure values are set properly
      setDetectedLang(res.data.detectedLang);
      setTranslatedText(res.data.translatedText);
    } catch (err) {
        console.error('Error:', err.response?.data || err.message);
        alert(err.response?.data?.error || 'Conversion failed.');
    }
  };

  return (
    <div>
      <h2>Convert Language</h2>
      <textarea
        rows="4"
        cols="50"
        placeholder="Type a sentence..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <select value={targetLang} onChange={(e) => setTargetLang(e.target.value)}>
        {languages.map((lang) => (
          <option key={lang} value={lang}>
            {lang}
          </option>
        ))}
      </select>
      <br />
      <button onClick={handleConvert}>Convert</button>

      {detectedLang && translatedText && (
        <div style={{ marginTop: '20px' }}>
          <p><strong>Detected Language:</strong> {detectedLang}</p>
          <p><strong>Translated Text:</strong> {translatedText}</p>
        </div>
      )}
    </div>
  );
};

export default Convert;
