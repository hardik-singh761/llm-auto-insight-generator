from flask import Flask, jsonify
import pandas as pd
from backend.statistics_generator import generate_statistics

app = Flask(__name__)

@app.route("/stats")
def stats():
    df = pd.read_csv("data/cleaned_data.csv")
    stats = generate_statistics(df)
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)