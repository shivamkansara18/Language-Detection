import React from 'react';
import { useNavigate } from 'react-router-dom';

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
    <div>
      <h2>Welcome, {user?.username || 'Guest'}</h2>
      <button onClick={() => navigate('/detect')}>Recognize Language</button>
      <button onClick={() => navigate('/convert')}>Convert Language</button>
      <button onClick={() => navigate('/history')}>History</button>
      <button onClick={() => navigate('/image-to-text')}>Image to Text</button>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default Dashboard;
