import streamlit as st
from ui import render_chat_ui
from utils import load_model, detect_license_plate

st.set_page_config(page_title="License Plate Detector", layout="centered")

# Title
st.title("📸 License Plate Detector")

# Load YOLO model (runs once)
model = load_model("./models/model.pt")

# Chat-like interface
render_chat_ui(model)
