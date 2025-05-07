

## 🧠 Devanagari Digit Recognition Web App

A simple and elegant web application built using **Flask** that lets users upload an image of a handwritten **Devanagari digit (0–9)** and predicts the digit using a trained deep learning model.

![screenshot](https://img.shields.io/badge/Flask-Python%203.x-blue?logo=flask)
![screenshot](https://img.shields.io/badge/Model-Keras%20%2B%20CNN-brightgreen)
![screenshot](https://img.shields.io/badge/UI-Bootstrap%205-orange)

---

### 🚀 Features

- Upload image through a simple web interface
- Preprocessing of input using Pillow
- Deep Learning model (.h5) prediction with Keras
- Responsive Bootstrap 5 frontend
- Clean result display with image preview

---

### 🗂️ Project Structure

```
devanagari_flask_app/
│
├── app.py                    # Flask backend
├── devanagari_digit_model.h5 # Trained CNN model (included in repo  😊)
├── static/
│   ├── uploads/              # Stores uploaded images
│   └── style.css             # Custom styles (optional)
└── templates/
    ├── index.html            # Upload form UI
    └── result.html           # Prediction result page
```

---

### ⚙️ Requirements

> You can install all dependencies using pip:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```txt
flask
tensorflow
numpy
pillow
```

---

### 💡 How to Run Locally

```bash
# Step 1: Clone the repo
git clone https://github.com/Bit-Nest/Devanagari-Digit-Recognition.git
cd devanagari-digit-recognition-flask

# Step 2: Make sure your model file is present
# Place your trained Keras .h5 model here:
# devanagari_digit_model.h5

# Step 3: Run the app
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

### 🧠 About the Model

- Trained on a dataset of handwritten Devanagari digits (`digit_0` to `digit_9`)
- CNN-based architecture
- Input shape: `(64, 64, 3)`

---


### 📦 Deployment

You can easily deploy this on:
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku](https://heroku.com/) *(legacy free tier deprecated)*
- AWS / EC2 / S3 static + API gateway

---


### 📄 License

This project is licensed under the MIT License.

---
