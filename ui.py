import streamlit as st
from utils import detect_license_plate, load_image_from_upload, load_image_from_url
import io
from PIL import Image
import numpy as np

def render_chat_ui(model):
    st.markdown("Chat-style license plate detector. Upload an image or paste a URL.")

    history = st.session_state.get("chat_history", [])
    input_mode = st.radio("Choose Input Type", ["Upload Image", "Image URL"])

    # Input
    uploaded_file = None
    image_url = None

    if input_mode == "Upload Image":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    else:
        image_url = st.text_input("Paste image URL")

    submit = st.button("Detect License Plate")

    if submit:
        if input_mode == "Upload Image" and uploaded_file is not None:
            image = load_image_from_upload(uploaded_file)
            label = "User uploaded an image."
        elif input_mode == "Image URL" and image_url.strip():
            image = load_image_from_url(image_url)
            label = f"User sent image URL: {image_url}"
        else:
            st.warning("Please provide a valid image.")
            return

        st.session_state.chat_history = history + [(label, image)]

        # Detect and display
        with st.spinner("Detecting license plate..."):
            result_img = detect_license_plate(model, image)
            st.image(result_img, caption="Bounding box", use_column_width=True)

        # Save result to history
        st.session_state.chat_history.append(("Bounding box", result_img))

    
