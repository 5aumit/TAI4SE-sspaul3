import io
import os
import cv2 

from google.cloud import vision

def non_ascii(text):
    return ''.join(i if ord(i)<128 and i.isalnum() else '' for i in text]).strip()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'apikey.json'

# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
path = os.path.join(os.path.dirname(__file__), '3.jpg') # Your image path from current directory 
client = vision.ImageAnnotatorClient()

image = cv2.imread(path)

# Encode the frame using CV2  functions
success, encoded_image = cv2.imencode('.jpg', image)
content2 = encoded_image.tobytes()

# OCR Image to text process
image_cv2 = vision.types.Image(content=content2)
response =  client.text_detection(image=image_cv2)
texts = response.text_annotations

full_text = non_ascii_remove(response.full_text_annotations)
print('Full Text:', full_text)

