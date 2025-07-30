# 🎯 AI Media Threat Detection App

This project uses AI to detect emotional expressions in images and videos, and potential threats in audio files, by analyzing facial emotions and spoken keywords.

## 🚀 Project Link

**Live App**: [Launch Now](https://huggingface.co/spaces/tollyboy88/AI_Media_Threat_Detection)

---

## 🧠 What does it do?

- **Image/Video Analysis**: Detect emotions like anger, fear, or happiness from faces.
- **Audio Analysis**: Transcribes audio and flags threatening keywords like *"kill"*, *"bomb"*, etc.

---

## 🔧 How was it built?

### Tech Stack:
- **Python**
- **Streamlit** for interactive UI
- **OpenCV** for image & video processing
- **Transformers (Whisper)** for audio transcription
- **Hugging Face Spaces** for cloud deployment

---

## 🗂️ Project Structure

```
.
├── .huggingface.yml          # Hugging Face config file (sets Streamlit as SDK)
├── requirements.txt          # Python dependencies
├── src/
│   ├── streamlit_app.py      # Main app logic (UI & routing)
│   └── utils/
│       ├── face_emotion.py   # Handles image/video emotion detection
│       └── audio_analysis.py # Handles Whisper audio analysis
```

---

## 🧪 How to run locally

```bash
# Clone the repo
git clone https://huggingface.co/spaces/tollyboy88/AI_Media_Threat_Detection
cd AI_Media_Threat_Detection

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run src/streamlit_app.py
```

---

## 📦 Deployment Info

This app runs on Hugging Face using the Streamlit SDK. The config is specified in `.huggingface.yml`:

```yaml
sdk: streamlit
app_file: src/streamlit_app.py
```

To deploy:
1. Push your code to Hugging Face.
2. The Space builds and launches automatically.
3. View logs for any issues in the “Logs” tab.

---

## 🤝 Acknowledgments

- Built by Adebayo Adetola
- Thanks to [Hugging Face](https://huggingface.co/spaces) and [OpenAI](https://openai.com) for APIs and tools

---

## 📬 Contact
adebayoadetola96@yahoo.com

Feel free to reach out for collaborations or feedback!

