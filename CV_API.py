from fastapi import FastAPI, UploadFile, File
import clip
import os
import io
import torch
import nest_asyncio
import uvicorn
from ultralytics import YOLO
from PIL import Image

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


detection_model = YOLO("yolov8n.pt")  # Object Detection

device = "cuda" if torch.cuda.is_available() else "cpu" # Object Classification with adjustable confidence thresholds
model, preprocess = clip.load("ViT-B/32", device=device)

categories = ["dog", "cat", "bird", "car", "person", "bicycle", "tree", "building", "food", "giraffe"]

text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in categories]).to(device)



@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    results = detection_model(image)
    
    allowed_objects = {"person", "car", "dog", "cat", "bicycle"} #Objects to detect
    
    
    detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x_min, y_min, x_max, y_max = map(int, box.xyxy[0])
            label = detection_model.names[int(box.cls[0])]  

            if label in allowed_objects:
                detections.append({
                    "label": label,
                    "x_min": x_min,
                    "y_min": y_min,
                    "x_max": x_max,
                    "y_max": y_max
                })

    return {"detections": detections}


@app.post("/classify/")
async def classify_image(file: UploadFile = File(...), confidence_threshold: float = 0.2):
    """Classify image and return all objects above a confidence threshold"""
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")


    image_tensor = preprocess(image).unsqueeze(0).to(device)

  
    with torch.no_grad():
        image_features = model.encode_image(image_tensor)
        text_features = model.encode_text(text_inputs)
        similarity = (image_features @ text_features.T).softmax(dim=-1)

    # Get all categories above confidence threshold
    detected_objects = {
        categories[i]: float(similarity[0, i])  # Convert tensor to float
        for i in range(len(categories)) if similarity[0, i] > confidence_threshold
    }
    
    return {"detected_objects": detected_objects}

nest_asyncio.apply()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
