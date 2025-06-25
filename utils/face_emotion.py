import cv2
from deepface import DeepFace

class FaceEmotionAnalyzer:
    def __init__(self):
        self.cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        return faces

    def analyze_emotion(self, face_img):
        try:
            result = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
            score = result[0]['emotion'][emotion]
            return emotion, score
        except Exception as e:
            print(f"[FaceEmotionAnalyzer] Error: {e}")
            return None, None