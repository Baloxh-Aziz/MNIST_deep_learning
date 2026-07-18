import streamlit as st
import requests
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image
import io

st.title("🔢 MNIST Digit Classifier")

BACKEND_URL = "https://hacker-ai-mnist.hf.space/predict"

tab1, tab2 = st.tabs(["✏️ Draw a Digit", "📁 Upload Image"])

with tab1:
    st.write("Draw a digit on the blackboard:")
    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=20,
        stroke_color="white",
        background_color="black",
        height=300,
        width=300,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("🔍 Predict Drawing"):
        if canvas_result.image_data is not None and np.sum(canvas_result.image_data) > 0:
            img = Image.fromarray(canvas_result.image_data.astype("uint8"))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)
            with st.spinner("Predicting..."):
                try:
                    response = requests.post(BACKEND_URL, files={"file": ("drawing.png", buf, "image/png")}, timeout=30)
                    response.raise_for_status()
                    result = response.json()
                    st.success(f"Predicted Digit: **{result['predicted_digit']}**")
                    st.write(f"Confidence: {result['confidence']}%")
                except requests.exceptions.RequestException as e:
                    st.error(f"Could not reach backend API: {e}")
        else:
            st.warning("Please draw a digit first!")

with tab2:
    st.write("Upload a digit image (0-9) and the model will predict it.")
    uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width=150)
        if st.button("🔍 Predict Upload"):
            with st.spinner("Predicting..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                try:
                    response = requests.post(BACKEND_URL, files=files, timeout=30)
                    response.raise_for_status()
                    result = response.json()
                    st.subheader(f"Predicted Digit: {result['predicted_digit']}")
                    st.write(f"Confidence: {result['confidence']}%")
                except requests.exceptions.RequestException as e:
                    st.error(f"Could not reach backend API: {e}")
