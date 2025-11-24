from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    signals = ["BUY", "SELL", "WAIT"]
    signal = random.choice(signals)
    return jsonify({
        "gold_signal": signal,
        "status": "running successfully"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
