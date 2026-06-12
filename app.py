from flask import Flask, request, render_template_string
from intent_model import predict_intent_with_confidence
from responses import base_response
from styles import apply_style

TEMPLATE = """
<!doctype html>
<title>Intent-Aware Response</title>
<h1>Ask a question</h1>
<form method=post>
  <textarea name=query rows=4 cols=60>{{query}}</textarea><br>
  <label for=style>Style:</label>
  <select name=style>
    <option>Genius</option>
    <option>Intern</option>
    <option>Professor</option>
    <option>Reviewer</option>
  </select>
  <button type=submit>Ask</button>
</form>
{% if result %}
<hr>
<p><strong>Detected Intent:</strong> {{intent}} ({{confidence:.2%}})</p>
<p><strong>Response:</strong> {{response}}</p>
{% endif %}
"""


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        query = ''
        result = None
        intent = ''
        confidence = 0.0
        response = ''
        if request.method == 'POST':
            query = request.form.get('query', '')
            style = request.form.get('style', '')
            intent, confidence = predict_intent_with_confidence(query)
            raw = base_response(intent)
            response = apply_style(style, raw)
            result = True
        return render_template_string(TEMPLATE, query=query, result=result, intent=intent, confidence=confidence, response=response)

    return app
