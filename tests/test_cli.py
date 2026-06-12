import subprocess
import sys
import os


def test_train_cli():
    # Run the script with --train
    p = subprocess.run([sys.executable, 'main.py', '--train'], capture_output=True, text=True)
    assert 'Training model from data.csv' in p.stdout
    assert 'Model trained and saved.' in p.stdout
