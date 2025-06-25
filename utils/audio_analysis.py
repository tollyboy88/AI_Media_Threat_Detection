import speech_recognition as sr

class AudioAnalyzer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.keywords = ['help', 'kill', 'gun', 'knife', 'danger', 'threat', 'don\'t hurt me']

    def listen_and_detect(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                transcript = self.recognizer.recognize_google(audio).lower()
                threats = [word for word in self.keywords if word in transcript]
                return transcript, threats
            except sr.UnknownValueError:
                return "", []
            except Exception as e:
                print("[Audio] Error:", e)
                return "", []