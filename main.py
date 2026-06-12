import os
import argparse

# Import local modules (they live in the project root)
from intent_model import predict_intent_with_confidence, train_model, save_model
from responses import base_response
from styles import apply_style


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true", help="Retrain the model from data.csv and save it")
    parser.add_argument("--web", action="store_true", help="Start a small web UI instead of CLI")
    args = parser.parse_args()

    if args.train:
        print("Training model from data.csv...")
        vec, m = train_model()
        save_model(vec, m)
        print("Model trained and saved.")
        return

    if args.web:
        # Defer flask import to runtime
        from app import create_app
        app = create_app()
        app.run(port=8501)
        return
    print("=" * 50)
    print("  Intent-Aware Response System")
    print("=" * 50)

    # Read user input
    query = input("\nEnter your question: ")

    print("\nChoose style (Genius / Intern / Professor / Reviewer):")
    style = input("> ").strip()

    intent, confidence = predict_intent_with_confidence(query)

    response = base_response(intent)
    final_output = apply_style(style, response)

    print("\n" + "-" * 50)
    print(f"Detected Intent: {intent} (confidence: {confidence:.2%})")
    print(f"Response: {final_output}")
    print("-" * 50)


if __name__ == "__main__":
    main()