import React from 'react';
import { useNavigate } from 'react-router-dom';
import './index.css';

const Dashboard = () => {
  const navigate = useNavigate();

  let user = {};
  try {
    user = JSON.parse(localStorage.getItem('user')) || {};
  } catch (e) {
    console.error("Invalid user JSON in localStorage", e);
    navigate('/');
  }

  const logout = () => {
    localStorage.clear();
    navigate('/');
  };

  return (
    <div className="dashboard-container">
      <h2>Welcome, {user?.username || 'Guest'}</h2>
      <div className="button-group">
        <button onClick={() => navigate('/detect')}>Recognize Language</button>
        <button onClick={() => navigate('/convert')}>Convert Language</button>
        <button onClick={() => navigate('/history')}>History</button>
        <button onClick={() => navigate('/image-to-text')}>Image to Text</button>
        <button onClick={logout} className="logout">Logout</button>
      </div>
    </div>
  );
};

export default Dashboard;
