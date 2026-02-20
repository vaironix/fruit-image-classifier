import os
import numpy as np
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static/uploads"
MODEL_PATH = "model/fruit_model.h5"
LABELS_PATH = "model/labels.txt"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = load_model(MODEL_PATH)

with open(LABELS_PATH, "r") as f:
    labels = f.read().splitlines()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    confidence = float(np.max(prediction) * 100)
    predicted_class = labels[np.argmax(prediction)]

    return jsonify({
        "result": predicted_class,
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
