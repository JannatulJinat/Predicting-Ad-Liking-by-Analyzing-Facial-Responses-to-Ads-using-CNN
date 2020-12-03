import cv2
from model import FacialExpressionModel
import numpy as np
import matplotlib.pyplot as plt

cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):
    graph = np.zeros(7)
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        #to test the system on any video, pass the path to the parameters instead of 0

    def __del__(self):
        print(VideoCamera.graph)
        emo = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
        fig = plt.figure(figsize=(10, 5))
        fig.canvas.set_window_title('Real time emotion detection')
        plt.bar(emo, VideoCamera.graph, color='cyan', width=0.4)
        plt.xlabel("Emotion")
        plt.title("Bar chart")
        plt.show()
        self.video.release()
        self.video=cv2.destroyAllWindows()
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_fr, 1.3, 5)
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]
            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            if pred == "Angry":
                VideoCamera.graph[0] += 1
            elif pred == "Disgust":
                VideoCamera.graph[1] += 1
            elif pred == "Fear":
                VideoCamera.graph[2] += 1
            elif pred == "Happy":
                VideoCamera.graph[3] += 1
            elif pred == "Neutral":
                VideoCamera.graph[4] += 1
            elif pred == "Sad":
                VideoCamera.graph[5] += 1
            elif pred == "Surprise":
                VideoCamera.graph[6] += 1

            cv2.putText(fr, pred, (x, y+h+20), font,0.75, (0, 0, 255), 2)
            cv2.rectangle(fr, (x, y), (x+w, y+h), (0, 0, 0), 2)

        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()