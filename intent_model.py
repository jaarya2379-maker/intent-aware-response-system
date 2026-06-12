
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Paths
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "data.csv"))
MODELS_DIR = os.path.join(BASE_DIR, "models")
VECTORIZER_PATH = os.path.join(MODELS_DIR, "vectorizer.joblib")
MODEL_PATH = os.path.join(MODELS_DIR, "model.joblib")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Training data not found at {DATA_PATH}. Make sure data.csv exists in the project root.")


def train_model():
    data = pd.read_csv(DATA_PATH)

    X = data["text"]
    y = data["intent"]

    vectorizer = TfidfVectorizer(stop_words="english")
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=200)
    model.fit(X_vec, y)

    return vectorizer, model


def save_model(vectorizer, model):
    os.makedirs(MODELS_DIR, exist_ok=True)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    joblib.dump(model, MODEL_PATH)


def load_model():
    vectorizer = joblib.load(VECTORIZER_PATH)
    model = joblib.load(MODEL_PATH)
    return vectorizer, model


# Load existing model if present, otherwise train and save for faster subsequent startup
if os.path.exists(VECTORIZER_PATH) and os.path.exists(MODEL_PATH):
    try:
        vectorizer, model = load_model()
    except Exception:
        # If load fails, retrain
        vectorizer, model = train_model()
        save_model(vectorizer, model)
else:
    vectorizer, model = train_model()
    save_model(vectorizer, model)


def predict_intent(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


def predict_intent_with_confidence(text):
    vec = vectorizer.transform([text])
    proba = model.predict_proba(vec)[0]
    intent = model.predict(vec)[0]
    confidence = float(max(proba))
    return intent, confidence
