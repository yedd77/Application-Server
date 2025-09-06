from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import uvicorn, io, json

# Load YOLOv8 model
model = YOLO("best.pt")

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        img = Image.open(io.BytesIO(await file.read()))
        results = model(img)

        if not results[0].boxes:  # no detections
            return {"success": True, "predictions": []}

        predictions = json.loads(results[0].tojson())
        return {"success": True, "predictions": predictions}

    except Exception as e:
        # Any error (bad image, etc.)
        return {"success": False, "error": str(e)}

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)