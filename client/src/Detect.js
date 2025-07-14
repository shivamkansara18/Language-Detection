import React, { useState } from "react";
import axios from "axios";
import './index.css';

const Detect = () => {
  const [text, setText] = useState("");
  const [detectedLang, setDetectedLang] = useState("");
  const [loading, setLoading] = useState(false);
  const user = JSON.parse(localStorage.getItem("user"));

  const handleSubmit = async (e) => {
    e.preventDefault();
    setDetectedLang("");
    setLoading(true);

    try {
      const res = await axios.post("http://localhost:5000/api/detection/analyze", {
        text,
        userId: user._id,
      });

      setDetectedLang(res.data.detectedLang);
    } catch (err) {
      console.error("Detection failed:", err.response?.data?.error || err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="detect-container">
      <h2 className="page-title">Language Detection</h2>
      <form onSubmit={handleSubmit} className="detect-form">
        <textarea
          rows="4"
          cols="50"
          placeholder="Enter a sentence..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
          className="text-area"
        />
        <br />
        <button type="submit" disabled={loading} className="submit-button">
          {loading ? "Detecting..." : "Detect Language"}
        </button>
      </form>

      {detectedLang && (
        <div className="result-container">
          <p><strong>Detected Language:</strong> {detectedLang}</p>
        </div>
      )}
    </div>
  );
};

export default Detect;
