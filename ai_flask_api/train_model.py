# train_model.py
import pandas as pd
import re
import string
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ------------------ Data Preprocessing ------------------
data = pd.read_csv("Language_Detection.csv")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data["Processed_Text"] = data["Text"].apply(preprocess_text)

# Tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data["Processed_Text"])
vocab_size = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(data["Processed_Text"])
max_len = 100
X = pad_sequences(sequences, maxlen=max_len)

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data["Language"])
num_classes = len(label_encoder.classes_)
y = to_categorical(y)

# Train-test split
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

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save the trained model to a file
model.save("language_model.h5")
print("Model saved as 'language_model.h5'")
