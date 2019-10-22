## this is a code snippet obtained from Google's Vision API Quickstart
## You can follow the tutorial in this link: https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-usage-python
## The code has been modified for the workshop purposes by Jim Mirzakhalov

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('data/riot.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations

# print('\nLabels:')
# for label in labels:
#      print(label.description)

# # Detecting safe speech
# response = client.safe_search_detection(image=image)
# safe = response.safe_search_annotation
# print('\nSafe Search: ')
# print(safe)

# # facial detection
# response = client.face_detection(image=image)
# faces = response.face_annotations

# # Names of likelihood from google.cloud.vision.enums
# likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
#                     'LIKELY', 'VERY_LIKELY')
# print('Faces:')

# for face in faces:
#     print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
#     print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
#     print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

#     vertices = (['({},{})'.format(vertex.x, vertex.y)
#                 for vertex in face.bounding_poly.vertices])

#     print('face bounds: {}'.format(','.join(vertices)))