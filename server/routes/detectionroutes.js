const express = require('express');
const axios = require('axios');
const Detection = require('../models/detection');
const router = express.Router();

router.post('/analyze', async (req, res) => {
    const { text, targetLang, userId } = req.body;
    try {
      const response = await axios.post('http://localhost:8000/predict', {
        text,
        target_lang: targetLang,
      });
  
      const { detectedLang, translatedText } = response.data;
  
      const detection = new Detection({
        userId,
        originalText: text,
        detectedLang,
        translatedText,
        targetLang
      });
      await detection.save();
  
      res.json({ detectedLang, translatedText });
    } catch (err) {
      console.error('Analyze error:', err.response?.data || err.message);
      res.status(500).json({ error: 'Detection failed' });
    }
  });
  

router.get('/history/:userId', async (req, res) => {
  try {
    const history = await Detection.find({ userId: req.params.userId }).sort({ timestamp: -1 });
    res.json(history);
  } catch (err) {
    res.status(500).json({ error: 'Fetching history failed' });
  }
});

module.exports = router;
