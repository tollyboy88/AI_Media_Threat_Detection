import smtplib
from email.message import EmailMessage

def send_email_alert(subject, body, to_email, screenshot_path=None):
    # Configuration — replace with your credentials or environment variables
    EMAIL = os.getenv("EMAIL_ADDRESS")
    PASSWORD = os.getenv("EMAIL_PASSWORD")  # Use app password if using Gmail

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(body)

    if screenshot_path:
        with open(screenshot_path, "rb") as f:
            file_data = f.read()
            file_name = screenshot_path.split("/")[-1]
            msg.add_attachment(file_data, maintype="image", subtype="jpeg", filename=file_name)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"[Email Alert] Sent to {to_email}")
    except Exception as e:
        print(f"[Email Alert] Failed to send: {e}")
