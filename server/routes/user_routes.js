const express = require('express');
const jwt = require('jsonwebtoken');
const User = require('../models/user');
const bcrypt = require('bcryptjs');
const router = express.Router();
const isAuthenticated = require('../authMiddleware');

router.get('/dashboard', isAuthenticated, (req, res) => {
    res.send('Welcome to the dashboard!');
  });

router.post('/register', async (req, res) => {
    try {
      const { name, email, password } = req.body; // ✅ change username → name
      const user = new User({ username: name, email, password }); // ✅ assign correctly
      await user.save();
      res.status(201).json({ message: 'User registered successfully' });
    } catch (err) {
      console.error("Registration error:", err); // helpful debug
      res.status(400).json({ message: 'Registration failed', error: err.message });
    }
  });
  

  router.post('/login', async (req, res) => {
    try {
      const { email, password } = req.body;
      const user = await User.findOne({ email });
      if (!user || !(await user.comparePassword(password))) {
        return res.status(401).json({ error: 'Invalid credentials' });
      }
      const token = jwt.sign({ id: user._id }, 'secret_key');
  
      res.json({
        token,
        user: {
          _id: user._id,
          username: user.username,
          email: user.email
        }
      });
    } catch (err) {
      res.status(500).json({ error: 'Login failed' });
    }
  });
  

module.exports = router;