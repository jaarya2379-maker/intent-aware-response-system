# Intent-Aware Response System

A small, fast prototype that detects user intent from text and returns a context-aware, styled response. It ships with a lightweight sklearn model (training on `data.csv`), a CLI, and an optional Flask web interface.

This repository is ideal for demos, experiments, or as a starting point for production features (model persistence, model versioning, richer UIs).

---

## Highlights

- Intent classification using TF-IDF + Logistic Regression (scikit-learn).
- Model persistence with joblib for instant startup after first run.
- Interactive CLI with multiple response styles (Genius / Intern / Professor / Reviewer).
- Optional small web UI (Flask) for quick demoing.
- Tests (pytest) to validate model save/load and CLI `--train` flow.

---

## Quick start

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure `data.csv` exists in the project root (a small sample is included).

4. Train the model (optional — first run will train automatically if no saved model is found):

```bash
python main.py --train
```

5. Run the CLI:

```bash
python main.py
```

Type your question and pick a style when prompted.

6. Run the web demo:

```bash
python main.py --web
```

Open http://127.0.0.1:8501 in your browser.

---

## Examples

Non-interactive test (simulate user input):

```bash
python main.py <<'EOF'
Explain machine learning
Professor
EOF
```

Force retrain and save model:

```bash
python main.py --train
```

Run the Flask demo UI:

```bash
python main.py --web
```

---

## Project layout

- `main.py` — CLI entrypoint with `--train` and `--web` flags.
- `intent_model.py` — Model training, persistence (joblib), and inference helpers.
- `responses.py` — Mapping of intent → base response.
- `styles.py` — Style transformations applied to base responses.
- `app.py` — Small Flask app used when running `--web`.
- `data.csv` — Training dataset (text,intent).
- `requirements.txt` — Python dependencies.
- `tests/` — pytest tests.
- `intent_model/models/` — (created at runtime) saved `vectorizer.joblib` and `model.joblib`.

---

## Development notes & suggestions

- Startup performance: after the first run `intent_model/models/` is created and subsequent runs load the model instead of retraining.
- To change the dataset, edit `data.csv` and run `python main.py --train` to rebuild saved artifacts.
- For productionization:
  - Add model versioning and a simple model registry.
  - Move from sklearn to a server-friendly format if needed (ONNX, TF SavedModel) for cross-language serving.
  - Add input validation and authentication for the web endpoint.

---

## Tests

Run the test suite with pytest:

```bash
pytest -q
```

You should see the tests pass (there are small smoke tests for training, saving, loading, and a CLI train check).

---

## Troubleshooting

- Missing `data.csv`: the code will raise a helpful FileNotFoundError; ensure the dataset is present at the repository root.
- Missing packages: rerun `pip install -r requirements.txt` inside the activated venv.
- If the model files become corrupted, delete the `intent_model/models/` directory and run `python main.py --train` to recreate them.

---

## Next steps (ideas)

- Save model metadata (version, dataset checksum, training time).
- Add more intents and richer responses (templates, multi-turn context).
- Add a polished frontend or Dockerfile for easy deployment.

---

If you want, I can:
- Move models to a top-level `models/` folder and add versioning.
- Add a Dockerfile and GitHub Actions CI with tests and linting.
- Improve the web UI with modern CSS and client-side validation.

Tell me which one you'd like and I'll implement it.
