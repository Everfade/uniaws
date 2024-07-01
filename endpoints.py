from http.client import HTTPException
from typing import Dict
from fastapi import APIRouter
from starlette import status
from util.pydantic import Image
import base64
from pydantic import BaseModel
from services import ObjectDetector
from typing import List

router = APIRouter()
results_store: Dict[str, Dict] = {}

class Image(BaseModel):
    id: str
    image_data: str

class DetectedObject(BaseModel):
    label: str
    accuracy: float

class DetectionResult(BaseModel):
    id: str
    objects: List[DetectedObject]

@router.post("/image", status_code=status.HTTP_201_CREATED, summary="Upload image.")
def image_detector(img: Image):
    # Decode the base64 image
    image_data = base64.b64decode(img.image_data)
    
    # Detect objects in the image
    objects = ObjectDetector.detect_objects(image_data)
    
    # Save the result in the store
    results_store[img.id] = {"id": img.id, "objects": objects}
    
    return {"id": img.id, "objects": objects}

@router.get("/image/{image_id}", response_model=DetectionResult, summary="Get detection result.")
def get_detection_result(image_id: str):
    if image_id in results_store:
        return results_store[image_id]
    else:
        raise HTTPException(status_code=404, detail="Result not found")