import os
import importlib
from intent_model import VECTORIZER_PATH, MODEL_PATH, train_model, save_model, load_model


def test_train_and_save(tmp_path):
    # Train on provided data.csv and save to models/ in project
    vec, model = train_model()
    save_model(vec, model)
    assert os.path.exists(VECTORIZER_PATH)
    assert os.path.exists(MODEL_PATH)

    # Now load and ensure objects are present
    vec2, model2 = load_model()
    assert vec2 is not None
    assert model2 is not None


def test_predict_intent():
    from intent_model import predict_intent_with_confidence
    intent, conf = predict_intent_with_confidence('Explain machine learning')
    assert isinstance(intent, str)
    assert isinstance(conf, float)
