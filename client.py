import requests
import base64
import uuid
from datetime import datetime

# URL of the FastAPI endpoint
url = "http://localhost:5000/exc3/image"

# Generate a unique ID using uuid library
unique_id = str(uuid.uuid4())

# Path to the input image
image_path = "input_folder/000000000016.jpg"

# Read and encode the image in base64
with open(image_path, "rb") as image_file:
    img_encoded = base64.b64encode(image_file.read()).decode('utf-8')

# Prepare the data payload
data = {"id": unique_id, "image_data": img_encoded}

# Make the POST request to the FastAPI endpoint
try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print(f"status_code: {response.status_code}")
    print(f"msg: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
