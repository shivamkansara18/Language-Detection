import React, { useState } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";
import './index.css';

const Register = () => {
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await axios.post("http://localhost:5000/api/users/register", formData);
      if (res.data) {
        alert("Registration successful! You can now login.");
        navigate("/");
      }
    } catch (err) {
      console.error("Registration failed:", err.response?.data?.message || err.message);
      setError(err.response?.data?.message || "Something went wrong.");
    }
  };

  return (
    <div className="container">
      <form className="form-card" onSubmit={handleSubmit}>
        <h2 className="form-title">Register</h2>
        {error && <p className="error">{error}</p>}
        <input name="name" type="text" placeholder="Name" value={formData.name} onChange={handleChange} required />
        <input name="email" type="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
        <input name="password" type="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
        <button type="submit">Register</button>
        <p className="footer-text">
          Already registered? <Link to="/">Login</Link>
        </p>
      </form>
    </div>
  );
};

export default Register;
