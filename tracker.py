import os
from email.mime.text import MIMEText
import smtplib

EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]
RECIPIENT = os.environ["RECIPIENT_EMAIL"]

msg = MIMEText(
    "🎉 Your ShopMy tracker is working.\n\nThis is a test email from GitHub Actions."
)

msg["Subject"] = "ShopMy Tracker Test"
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECIPIENT

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(
        EMAIL_ADDRESS,
        RECIPIENT,
        msg.as_string()
    )

print("Email sent")
