import smtplib
from email.mime.text import MIMEText

SMTP_HOST = 'localhost'
SMTP_HOST_PORT = 1025
FROM_EMAIL = 'admin@placementportal.com'
subject = 'Welcome to the Placement Portal'
body = 'Thank you for registering on the Placement Portal. We are excited to have you on board!'

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email

    with smtplib.SMTP(SMTP_HOST, SMTP_HOST_PORT) as server:
        server.send_message(msg)