# import json
from flask import Flask, jsonify, request, Response
# import mediapipe as mp
# import numpy as np 
# import cv2
import sys

app = Flask(__name__)

# def get_prediction(image):
#     # image = Image.open(image_bytes)
#     # plt.imshow(image)
#     # plt.show()
#     mp_pose = mp.solutions.pose
#     print(image.shape, file=sys.stderr)
#     with mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=2) as pose:
#         results = pose.process(image)
#         if not results.pose_landmarks:
#                 print()
#     return results.pose_landmarks.landmark


@app.route('/')
def hello():
    return 'Hello World!'


# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         r = request
#         # convert string of image data to uint8
#         nparr = np.fromstring(r.data, np.uint8)
#         # decode image
#         img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#         # file = request.files['file'].stream
#         # img_bytes = file.read()
#         landmarks = get_prediction(img)

#         print(landmarks, file=sys.stderr)
#         print(landmarks[0], file=sys.stderr)
#         # d = {0:[landmarks[0].x, landmarks[0].y]}
#         d = {}
#         for i,l in enumerate(landmarks):
#             d[i] = [l.x, l.y]
#         print(d, file=sys.stderr)
#         json_landmarks = json.dumps(d)
#         print('json_landmarks:', json_landmarks , file=sys.stderr)
#         # response = {'landmarks': landmarks}
#         # encode response using jsonpickle
#         # response_pickled = jsonpickle.encode(response)
#         # return Response(response=response_pickled, status=200, mimetype="application/json")
#         return json_landmarks

if __name__ == '__main__':
    app.run(debug=True)