import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './index.css';

const HistoryPage = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const user = localStorage.getItem('email') || 'guest';
    axios.post('http://localhost:8000/history', { user })
      .then(res => setHistory(res.data))
      .catch(err => console.error("Failed to fetch history", err));
  }, []);

  return (
    <div className="history-page-container">
      <h2 className="page-title">Translation & Detection History</h2>
      <table className="history-table">
        <thead>
          <tr>
            <th>Original Text</th>
            <th>Detected Language</th>
            <th>Target Language</th>
            <th>Translated Text</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {history.map((entry, idx) => (
            <tr key={idx}>
              <td>{entry.text}</td>
              <td>{entry.detected_lang}</td>
              <td>{entry.target_lang}</td>
              <td>{entry.translated_text}</td>
              <td>{entry.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HistoryPage;
