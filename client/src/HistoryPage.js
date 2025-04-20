import React, { useEffect, useState } from 'react';
import axios from 'axios';

const HistoryPage = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const user = localStorage.getItem('email') || 'guest';
    axios.post('http://localhost:8000/history', { user })
      .then(res => setHistory(res.data))
      .catch(err => console.error("Failed to fetch history", err));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Translation & Detection History</h2>
      <table className="min-w-full border border-gray-300">
        <thead className="bg-gray-100">
          <tr>
            <th className="border px-4 py-2">Original Text</th>
            <th className="border px-4 py-2">Detected Language</th>
            <th className="border px-4 py-2">Target Language</th>
            <th className="border px-4 py-2">Translated Text</th>
            <th className="border px-4 py-2">Time</th>
          </tr>
        </thead>
        <tbody>
          {history.map((entry, idx) => (
            <tr key={idx}>
              <td className="border px-4 py-2">{entry.text}</td>
              <td className="border px-4 py-2">{entry.detected_lang}</td>
              <td className="border px-4 py-2">{entry.target_lang}</td>
              <td className="border px-4 py-2">{entry.translated_text}</td>
              <td className="border px-4 py-2">{entry.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HistoryPage;
