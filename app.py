import streamlit as st
import requests

st.title("MNIST Digit Classifier")
st.write("Upload a digit image (0-9) and the model will predict it.")

BACKEND_URL = "https://huggingface.co/spaces/hacker-ai/MNIST"

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=150)

    if st.button("Predict"):
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
