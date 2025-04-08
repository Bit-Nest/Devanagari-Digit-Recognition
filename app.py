import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image, ImageOps

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the model
model = load_model('devanagari_digit_model.h5')

# Class labels
labels = [f"Digit {i}" for i in range(10)]

def preprocess_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = ImageOps.fit(img, (64, 64), Image.Resampling.LANCZOS)
    img_array = np.array(img) / 255.0
    return img_array.reshape(1, 64, 64, 3)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    processed = preprocess_image(filepath)
    prediction = model.predict(processed)
    predicted_label = labels[np.argmax(prediction)]

    return render_template('result.html',
                           filename=filename,
                           label=predicted_label)

@app.route('/uploads/<filename>')
def send_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
