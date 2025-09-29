from ultralytics import YOLO
import numpy as np
import cv2
import tempfile
import requests
from PIL import Image
import os
import streamlit as st

@st.cache_resource
def load_model(model_path):
    """Load the trained YOLOv8 model."""
    return YOLO(model_path)

def detect_license_plate(model, image: np.ndarray) -> np.ndarray:
    """Detect license plate and return image with drawn bounding boxes."""
    results = model.predict(image, conf=0.25)
    annotated = results[0].plot()  # Draw boxes on the image
    return annotated

def load_image_from_upload(uploaded_file) -> np.ndarray:
    """Load image from an uploaded file."""
    image = Image.open(uploaded_file).convert("RGB")
    return np.array(image)

def load_image_from_url(url: str) -> np.ndarray:
    """Download and convert an image from a URL."""
    response = requests.get(url)
    img_arr = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
