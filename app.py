from flask import Flask, request, jsonify
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf
import numpy as np

# Load model and tokenizer
model = TFAutoModelForSequenceClassification.from_pretrained("./saved_model", from_pt=True)
tokenizer = AutoTokenizer.from_pretrained("./saved_model")
labels = ["negative", "neutral", "positive"]

app = Flask(__name__)

def predict(text):
    inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True)
    logits = model(inputs).logits
    probs = tf.nn.softmax(logits, axis=-1).numpy()[0]
    pred_class = np.argmax(probs)
    return {"label": labels[pred_class], "confidence": float(probs[pred_class])}

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    text = data.get("text", "")
    if text == "":
        return jsonify({"error": "No text provided"}), 400
    return jsonify(predict(text))

if __name__ == "__main__":
    app.run(debug=True)
