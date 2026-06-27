---
title: MNIST Frontend
emoji: 🎨
colorFrom: indigo
colorTo: pink
sdk: docker
app_port: 7860
pinned: false
---

# MNIST Frontend (Streamlit)

Streamlit UI jo image upload karke backend FastAPI Space ko call karta hai.

⚠️ **Important:** `app.py` mein `BACKEND_URL` ko apne deployed backend Space ke URL se replace karo, e.g.:
```
https://<username>-mnist-backend.hf.space/predict
```
