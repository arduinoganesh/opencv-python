from PIL import Image
import face_recognition
import numpy as np
import cv2

# loading and converting the image into numpy array
image = cv2.imread("presidents.jpg")

# Find all the faces in the image using the library
face_locations = face_recognition.face_locations(image)

# printing the number of items in the array
print("I found {} face(s) in this photograph".format(len(face_locations)))

for face_location in face_locations:

	#print location of each face in this image
	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

	#access and show each face in the image
	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()

