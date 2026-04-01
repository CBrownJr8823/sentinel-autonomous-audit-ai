import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class SentinelOutreach:
    def send_dispute(self, recipient_email, subject, body):
        sender_email = os.getenv("SENTINEL_EMAIL")
        sender_password = os.getenv("SENTINEL_EMAIL_PASSWORD") # Use an App Password!
        
        if not sender_email or not sender_password:
            return "Error: Email credentials not configured in .env"

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            return "✅ Dispute sent successfully!"
        except Exception as e:
            return f"❌ Failed to send: {str(e)}"
