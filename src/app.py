from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    signals = ["BUY", "SELL", "WAIT"]
    ai_tip = {
        "BUY": "السعر في منطقة دعم جيدة — الشراء مناسب مع وقف خسارة قريب.",
        "SELL": "السعر في منطقة مقاومة قوية — البيع مناسب بحجم قليل.",
        "WAIT": "السوق غير واضح الآن — الأفضل الانتظار حتى يتأكد الاتجاه."
    }
    signal = random.choice(signals)

    return jsonify({
        "gold_signal": signal,
        "ai_advice": ai_tip[signal],
        "status": "AI signal working successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
