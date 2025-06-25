import cv2
import os
import csv
import threading
import time
from datetime import datetime
from utils.face_emotion import FaceEmotionAnalyzer
from utils.audio_analysis import AudioAnalyzer
from utils.email_alert import send_email_alert

# Config
log_file = "threat_log.csv"
screenshot_dir = "screenshots"
ALERT_EMAIL = "recipient@example.com"  # Change to your alert destination

# Ensure necessary files/dirs
if not os.path.exists(log_file):
    with open(log_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Threat Type", "Details"])

os.makedirs(screenshot_dir, exist_ok=True)

# Initialize analyzers
face_analyzer = FaceEmotionAnalyzer()
audio_analyzer = AudioAnalyzer()
cap = cv2.VideoCapture(0)

# Trackers
audio_threats = []
last_emotion = ""

def save_screenshot(frame, tag):
    filename = f"{screenshot_dir}/screenshot_{tag}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(filename, frame)
    return filename

def log_threat(threat_type, details, screenshot_path=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, threat_type, details])
    send_email_alert(
        subject=f"🚨 Threat Detected: {threat_type}",
        body=f"Type: {threat_type}\nTime: {timestamp}\nDetails: {details}",
        to_email=ALERT_EMAIL,
        screenshot_path=screenshot_path
    )
    print(f"[LOGGED] {threat_type}: {details}")

# Background thread to listen for threats
def listen_audio_background():
    global audio_threats
    while True:
        transcript, threats = audio_analyzer.listen_and_detect()
        if threats:
            audio_threats = threats
            screenshot = save_screenshot(current_frame.copy(), "audio")
            log_threat("Audio", ', '.join(threats), screenshot_path=screenshot)
        time.sleep(1)

# Start audio thread
audio_thread = threading.Thread(target=listen_audio_background, daemon=True)
audio_thread.start()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_frame = frame.copy()
    faces = face_analyzer.detect_faces(frame)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        emotion, score = face_analyzer.analyze_emotion(face_img)
        if emotion:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
            cv2.putText(frame, f"{emotion} ({score:.1f}%)", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            if emotion in ["fear", "sad", "angry"] and emotion != last_emotion:
                last_emotion = emotion
                screenshot = save_screenshot(current_frame, "emotion")
                log_threat("Facial Emotion", emotion, screenshot_path=screenshot)

    if audio_threats:
        cv2.putText(frame, f"Audio Threat: {', '.join(audio_threats)}", (30, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow("AI Threat Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()