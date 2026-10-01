# 🔢 MNIST Digit Classifier

A deep learning web app that recognizes handwritten digits (**0–9**). Draw a digit on the canvas or upload an image, and the model predicts the digit along with its confidence.

👉 [Live Demo](https://mnist-deeplearning.streamlit.app/)
---

## ✨ Features

- ✏️ **Draw a digit** on a blackboard-style canvas
- 📁 **Upload an image** (PNG / JPG / JPEG) of a digit
- Shows the **predicted digit** and **confidence (%)**
- Friendly warnings if nothing is drawn or the backend is unreachable

---

## ⚙️ How It Works

1. The Streamlit frontend (`app.py`) captures your drawing or uploaded image.
2. The image is sent to a prediction API hosted on **Hugging Face Spaces**.
3. The trained **deep learning model (TensorFlow)** returns the predicted digit and confidence.
4. The result is displayed in the app.

Model trained on the classic **MNIST** dataset of handwritten digits.

---

## 🛠️ Tech Stack

`Python` `TensorFlow` `Streamlit` `NumPy` `Pillow` `streamlit-drawable-canvas`

---

## 🚀 Run Locally

```bash
git clone https://github.com/Baloxh-Aziz/MNIST_deep_learning.git
cd MNIST_deep_learning
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
MNIST_deep_learning/
├── app.py             # Streamlit frontend
├── requirements.txt   # Dependencies
├── .streamlit/        # Streamlit config
└── .devcontainer/     # Dev container config
```

---

## 💡 Tips for Best Results

- Draw the digit **large and centered**.
- Use a thick stroke (white on black works best, like MNIST images).

---

## 👤 Author

**Azizullah Asad** — BS Data Science Student
[GitHub](https://github.com/Baloxh-Aziz) · [LinkedIn](https://www.linkedin.com/in/azizullah-asad-203789345)
