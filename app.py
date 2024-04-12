import requests
import io
from PIL import Image
j = input("Enter the text: ")
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

j = image_bytes = query({
    "inputs": j,
})

# Create PIL Image object
image = Image.open(io.BytesIO(image_bytes))

# Save the image as a .png file
image.save("/workspaces/Subway-Surfersh/image.png", "PNG")
