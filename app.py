from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    html = f"<h3> TODO...</h3>"
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """Predicts something"""

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    #prediction = mlib.predict(json_payload["Weight"])
    return #jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)