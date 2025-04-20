from flask import Flask, request, jsonify
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

lang_map = {
    "English": "en", "Malayalam": "ml", "Hindi": "hi", "Tamil": "ta",
    "Kannada": "kn", "French": "fr", "Spanish": "es", "Portuguese": "pt",
    "Italian": "it", "Russian": "ru", "Sweedish": "sv", "Dutch": "nl",
    "Arabic": "ar", "Turkish": "tr", "German": "de", "Danish": "da", "Greek": "el"
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    target_lang_name = data.get("target_lang", "")

    if not text or not target_lang_name:
        return jsonify({"error": "Missing text or target language"}), 400

    try:
        detected_lang_code = detect(text)
        target_lang_code = lang_map.get(target_lang_name)

        if not target_lang_code:
            return jsonify({"error": "Invalid target language"}), 400

        translated = translator.translate(text, src=detected_lang_code, dest=target_lang_code)
        return jsonify({
            "detectedLang": translated.src,
            "translatedText": translated.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000)
