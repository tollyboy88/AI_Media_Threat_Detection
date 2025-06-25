import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="AI Safety Dashboard", layout="wide")
st.title("🔐 AI Safety Monitoring Dashboard")

# --------------------
# Setup log file path
log_file = "threat_log.csv"

# Auto-create CSV if missing or empty
if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
    with open(log_file, "w") as f:
        f.write("Timestamp,Threat Type,Details\n")

# Load threat log safely
try:
    df = pd.read_csv(log_file)
    if not df.empty:
        st.subheader("📝 Threat Log")
        st.dataframe(df.sort_values(by='Timestamp', ascending=False), use_container_width=True)
    else:
        st.info("No threat logs recorded yet.")
except Exception as e:
    st.error(f"Failed to load log file: {e}")

# --------------------
# Display screenshots
screenshot_dir = "screenshots"
st.subheader("🖼️ Captured Threat Screenshots")

if os.path.exists(screenshot_dir):
    images = sorted([f for f in os.listdir(screenshot_dir) if f.endswith(".jpg")], reverse=True)
    if images:
        cols = st.columns(3)
        for i, img_file in enumerate(images[:9]):
            img_path = os.path.join(screenshot_dir, img_file)
            image = Image.open(img_path)
            cols[i % 3].image(image, caption=img_file, use_column_width=True)
    else:
        st.info("No screenshots available yet.")
else:
    st.info("Screenshot folder not found.")

# --------------------
# Upload for future extension
st.subheader("📤 Upload Media for Manual Review (Coming Soon)")
st.file_uploader("Choose a video or audio file", type=["mp4", "mp3", "wav", "mov"])
