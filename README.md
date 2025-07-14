Language Detection & Translation using NLP

A powerful end-to-end solution that detects the language of typed or scanned text (OCR) across 17 languages using NLP techniques, and translates it into the user’s desired language using Google Translate API. The system is web-based, fully deployed on AWS, and supports image-based text extraction as well.


1.  Objectives
Build a machine learning model to accurately detect languages from text.

Integrate with the Google Translate API to convert text into any target language.

Support image-based input using OCR for detecting and translating text from screenshots or photos.

Deploy the full system in the cloud using Dockerized services on AWS EC2 for real-time, web-based interaction.


2.  Technologies Used
Languages: Python, JavaScript (Node.js, React)

Machine Learning: Scikit-learn (Bag-of-Words, Naive Bayes), TensorFlow (for OCR)

Frontend: React.js

Backend: Node.js + Express

Model API: Flask (Python)

Translation: Google Translate API

OCR: TensorFlow + Tesseract

Cloud Deployment: AWS EC2 (2 instances), Docker

Database: MongoDB Atlas


3.  Key Features
 Language Detection: Predicts the language of a given text with 90.2% accuracy over 17 supported languages.

 Translation: Converts detected text into any user-selected language using Google Translate.

 OCR Support: Users can upload screenshots or images with text; the system extracts text before processing.

 Dockerized Deployment: Each component (frontend, backend, and model API) is containerized and deployed via Docker.

 Scalable Cloud Hosting: Hosted using two AWS EC2 instances — one for the ML model (Flask API), another for the MERN stack.


4.  Project Structure
   
.

├── client/                         # React frontend

│   ├── components/                # Convert, Detect, OCR, History UI

│   ├── App.js                     # Routes and main layout

│   └── style.css                  # Custom dark theme styling


├── server/                         # Express backend

│   ├── routes/                   # API endpoints

│   ├── models/                   # MongoDB models

│   └── server.js                 # Entry point


├── ai_flask_api/                   # Flask API for language detection and OCR

│   ├── app.py                    # Model serving (text + image)

│   ├── language_model.h5         # Trained model

│   └── train_model.py            # Training script


├── docker-compose.yml             # Multi-container setup

├── README.md                      # Project documentation


5.  Deployment Overview
Instance 1: Hosts the Flask-based ML model and OCR handler
URL: http://65.2.122.171:8000/

Instance 2: Hosts the MERN stack frontend + backend
URLs:

Frontend: http://52.66.251.84:3000/

Backend: http://52.66.251.84:3001/

Database: MongoDB Atlas (Cloud)


6.  Accuracy
Language Detection Accuracy: 90.2% on validation set across 17 languages.

Model trained using Bag-of-Words + Multinomial Naive Bayes with optimized preprocessing.


7.  Image-Based Detection Workflow
User uploads an image containing text.

OCR engine extracts text using TensorFlow.

Text is passed through the language detection model.

Detected text is translated to the target language.


8.  Live Demo & GitHub
 View Project on GitHub
 Want to test it live? Just ask and I can help you deploy a live test version.


9.  Future Enhancements
Integrate speech-to-text input for audio-based language detection.

Enable PDF file uploads for document-based detection and translation.

Add language auto-detection on frontend input field.

Create a user dashboard with saved translation history and analytics.
