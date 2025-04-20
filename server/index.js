const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const userRoutes = require('./routes/user_routes');
const detectionRoutes = require('./routes/detectionroutes');

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/langdetect', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log('MongoDB connected'));

app.use('/api/users', userRoutes);
app.use('/api/detection', detectionRoutes);

app.listen(5000, () => console.log('Server running on port 5000'));
