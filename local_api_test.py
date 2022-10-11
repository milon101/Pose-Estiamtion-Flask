from __future__ import print_function
import requests
import json
import cv2

addr = 'https://pose-estimation-flask.herokuapp.com/'
# addr = "http://192.168.0.74:5000/"
# addr = "http://127.0.0.1:5000/"
test_url = addr + '/predict'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('input_image.jpeg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)
# decode response
print(response.text, response.status_code)
# print(json.loads(response.text))
landmarks = json.loads(response.text)
print(landmarks)
print('first_landmark :', landmarks['0'])