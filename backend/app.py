from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import json
import pandas as pd

from backend.pipeline import run_pipeline
from visualization.chart_generator import generate_chart

app = Flask(__name__, template_folder="../templates", static_folder="../static")

UPLOAD_FOLDER = "data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    charts = request.form.get("charts")

    if charts:
        charts = json.loads(charts)
    else:
        charts = None

    insights = run_pipeline(filepath, charts)

    return jsonify(insights)


@app.route('/charts/<path:filename>')
def serve_chart(filename):
    return send_from_directory('../visualization/outputs', filename)




if __name__ == "__main__":
    app.run(debug=True)