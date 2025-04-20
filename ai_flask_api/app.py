# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import numpy as np
# import pandas as pd
# import re
# import string
# from datetime import datetime
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Embedding, GlobalAveragePooling1D
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.utils import to_categorical
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from translate import Translator

# # ------------------ Data Preprocessing ------------------

# data = pd.read_csv("Language_Detection.csv")

# def preprocess_text(text):
#     text = text.lower()
#     text = re.sub(r'\d+', '', text)
#     text = text.translate(str.maketrans("", "", string.punctuation))
#     text = re.sub(r'\s+', ' ', text).strip()
#     return text

# data["Processed_Text"] = data["Text"].apply(preprocess_text)

# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(data["Processed_Text"])
# vocab_size = len(tokenizer.word_index) + 1
# sequences = tokenizer.texts_to_sequences(data["Processed_Text"])
# max_len = 100
# X = pad_sequences(sequences, maxlen=max_len)

# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(data["Language"])
# num_classes = len(label_encoder.classes_)
# y = to_categorical(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # ------------------ Model ------------------

# model = Sequential([
#     Embedding(input_dim=vocab_size, output_dim=64, input_length=max_len),
#     GlobalAveragePooling1D(),
#     Dense(128, activation='relu'),
#     Dropout(0.5),
#     Dense(64, activation='relu'),
#     Dropout(0.3),
#     Dense(num_classes, activation='softmax')
# ])

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# # ------------------ Flask App ------------------

# app = Flask(__name__)
# CORS(app)

# # In-memory user history storage
# user_history = {}

# # Language code map for translation
# lang_code_map = {
#     'English': 'en', 'Malayalam': 'ml', 'Hindi': 'hi', 'Tamil': 'ta',
#     'Kannada': 'kn', 'French': 'fr', 'Spanish': 'es', 'Portuguese': 'pt',
#     'Italian': 'it', 'Russian': 'ru', 'Sweedish': 'sv', 'Dutch': 'nl',
#     'Arabic': 'ar', 'Turkish': 'tr', 'German': 'de', 'Danish': 'da', 'Greek': 'el'
# }

# # Translate text
# def translate_text(text, src_lang, dest_lang):
#     try:
#         translator = Translator(from_lang=src_lang, to_lang=dest_lang)
#         translation = translator.translate(text)
#         return translation
#     except Exception as e:
#         return f"Translation error: {str(e)}"

# # Predict language and translate
# def predict_and_translate(text, target_lang='en'):
#     processed_text = preprocess_text(text)
#     sequence = tokenizer.texts_to_sequences([processed_text])
#     padded_sequence = pad_sequences(sequence, maxlen=max_len)
#     prediction = model.predict(padded_sequence, verbose=0)
#     predicted_class = np.argmax(prediction)
#     detected_lang = label_encoder.inverse_transform([predicted_class])[0]

#     src_code = lang_code_map.get(detected_lang, 'auto')
#     tgt_code = lang_code_map.get(target_lang, 'en')

#     if src_code != tgt_code:
#         translated_text = translate_text(text, src_code, tgt_code)
#         return detected_lang, translated_text
#     return detected_lang, text

# # --------------- Routes -----------------

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     text = data.get('text', '')
#     target_lang = data.get('target_lang', 'English')
#     user = data.get('user', 'guest')

#     if not text or not target_lang:
#         return jsonify({"error": "Missing required fields"}), 400

#     detected_lang, translated_text = predict_and_translate(text, target_lang)

#     entry = {
#         'text': text,
#         'detected_lang': detected_lang,
#         'translated_text': translated_text,
#         'target_lang': target_lang,
#         'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     }

#     if user not in user_history:
#         user_history[user] = []
#     user_history[user].append(entry)

#     return jsonify({
#         'detectedLang': detected_lang,
#         'translatedText': translated_text
#     })

# @app.route('/history', methods=['POST'])
# def get_history():
#     data = request.get_json()
#     user = data.get('user', 'guest')
#     return jsonify(user_history.get(user, []))

# # ----------------- Main ------------------

# if __name__ == '__main__':
#     app.run(port=8000)



from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import re
import string
from datetime import datetime
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from translate import Translator
from PIL import Image
import pytesseract
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ------------------ Data Preprocessing ------------------

data = pd.read_csv("Language_Detection.csv")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data["Processed_Text"] = data["Text"].apply(preprocess_text)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(data["Processed_Text"])
vocab_size = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(data["Processed_Text"])
max_len = 100
X = pad_sequences(sequences, maxlen=max_len)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data["Language"])
num_classes = len(label_encoder.classes_)
y = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ------------------ Model ------------------

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=64, input_length=max_len),
    GlobalAveragePooling1D(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# ------------------ Flask App ------------------

app = Flask(__name__)
CORS(app)

# In-memory user history storage
user_history = {}

# Language code map for translation
lang_code_map = {
    'English': 'en', 'Malayalam': 'ml', 'Hindi': 'hi', 'Tamil': 'ta',
    'Kannada': 'kn', 'French': 'fr', 'Spanish': 'es', 'Portuguese': 'pt',
    'Italian': 'it', 'Russian': 'ru', 'Sweedish': 'sv', 'Dutch': 'nl',
    'Arabic': 'ar', 'Turkish': 'tr', 'German': 'de', 'Danish': 'da', 'Greek': 'el'
}

# Translate text
def translate_text(text, src_lang, dest_lang):
    try:
        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {str(e)}"

# Predict language and translate
def predict_and_translate(text, target_lang='en'):
    processed_text = preprocess_text(text)
    sequence = tokenizer.texts_to_sequences([processed_text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len)
    prediction = model.predict(padded_sequence, verbose=0)
    predicted_class = np.argmax(prediction)
    detected_lang = label_encoder.inverse_transform([predicted_class])[0]

    src_code = lang_code_map.get(detected_lang, 'auto')
    tgt_code = lang_code_map.get(target_lang, 'en')

    if src_code != tgt_code:
        translated_text = translate_text(text, src_code, tgt_code)
        return detected_lang, translated_text
    return detected_lang, text

# --------------- Routes -----------------

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'English')
    user = data.get('user', 'guest')

    if not text or not target_lang:
        return jsonify({"error": "Missing required fields"}), 400

    detected_lang, translated_text = predict_and_translate(text, target_lang)

    entry = {
        'text': text,
        'detected_lang': detected_lang,
        'translated_text': translated_text,
        'target_lang': target_lang,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    if user not in user_history:
        user_history[user] = []
    user_history[user].append(entry)

    return jsonify({
        'detectedLang': detected_lang,
        'translatedText': translated_text
    })

@app.route('/history', methods=['POST'])
def get_history():
    data = request.get_json()
    user = data.get('user', 'guest')
    return jsonify(user_history.get(user, []))

@app.route('/predict-image', methods=['POST'])
def predict_from_image():
    file = request.files.get('image')
    target_lang = request.form.get('target_lang', 'English')
    user = request.form.get('user', 'guest')

    if not file:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)

        if not text.strip():
            return jsonify({"error": "No text detected in image"}), 400

        detected_lang, translated_text = predict_and_translate(text, target_lang)

        entry = {
            'text': text,
            'detected_lang': detected_lang,
            'translated_text': translated_text,
            'target_lang': target_lang,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'source': 'image'
        }

        if user not in user_history:
            user_history[user] = []
        user_history[user].append(entry)

        return jsonify({
            'detectedLang': detected_lang,
            'translatedText': translated_text,
            'originalText': text.strip()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/image-to-text', methods=['POST'])
def image_to_text():
    try:
        if 'image' not in request.files:
            app.logger.error("No image part in the request")
            return jsonify({"error": "No image uploaded"}), 400

        image = request.files['image']
        app.logger.info(f"Image received: {image.filename}")
        image_bytes = image.read() 
        img = Image.open(io.BytesIO(image_bytes))
        app.logger.info("Image successfully opened")

        text = pytesseract.image_to_string(img)
        if not text.strip():
            return jsonify({"error": "No text detected in image"}), 400

        processed_text = preprocess_text(text)
        sequence = tokenizer.texts_to_sequences([processed_text])
        padded_sequence = pad_sequences(sequence, maxlen=max_len)
        prediction = model.predict(padded_sequence, verbose=0)
        predicted_class = np.argmax(prediction)
        detected_lang = label_encoder.inverse_transform([predicted_class])[0]

        return jsonify({"text": text.strip(), "detectedLang": detected_lang})
    
    except Exception as e:
        app.logger.error(f"Exception in image-to-text route: {e}")
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500


# ----------------- Main ------------------

if __name__ == '__main__':
    app.run(port=8000)
