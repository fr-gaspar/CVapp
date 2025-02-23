# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 02:39:59 2025

@author: FGaspar
"""

import streamlit as st
import requests
import io
from PIL import Image, ImageDraw

# FastAPI Server URL
API_URL = "https://cv-backend-lc0e.onrender.com"

st.title("Computer Vision Interface")
st.write("Upload an image and choose an action")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

task = st.radio("Select Task", ["Object Detection", "Image Classification"])

confidence_threshold = None
if task == "Image Classification":
    confidence_threshold = st.slider("Confidence Threshold", 0.05, 0.9, 0.2, 0.05)


if st.button("Analyze Image") and uploaded_file:
    
    image_bytes = uploaded_file.getvalue()

   
    if task == "Object Detection":
        endpoint = f"{API_URL}/detect/"
        params = {}  # Needed because of classify even though detection doesn't require aditional parameters
    else:
        endpoint = f"{API_URL}/classify/"
        params = {"confidence_threshold": confidence_threshold}  

    files = {"file": (uploaded_file.name, image_bytes, uploaded_file.type)}
    response = requests.post(endpoint, files=files, params=params)

    if response.status_code == 200:
        result = response.json()

        if task == "Object Detection":
            st.write("### Detection Results")

            
            img = Image.open(io.BytesIO(image_bytes))
            draw = ImageDraw.Draw(img)

            for detection in result["detections"]:
                label = detection["label"]
                x_min, y_min, x_max, y_max = detection["x_min"], detection["y_min"], detection["x_max"], detection["y_max"]

                
                draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)

                
                draw.text((x_min, y_min - 10), label, fill="red")

            # Show image
            st.image(img, caption="Detected Objects", use_container_width=True)

        else:
            st.write("### Classification Results")
            detected_objects = result.get("detected_objects", {})

            if detected_objects:
                st.success("Detected Objects:")
                for obj, confidence in detected_objects.items():
                    st.write(f"- **{obj}** ({confidence:.2f} confidence)")
            else:
                st.warning("No objects detected above the confidence threshold.")
    else:
        st.error("Error: Could not process the image.")
