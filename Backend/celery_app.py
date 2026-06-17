from celery import Celery

celery = Celery('task', broker='redis://localhost:6379/0')


celery.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
) 

from app import app
import time
from mail import send_email

@celery.task
def example_task():
    with app.app_context():
        time.sleep(5) 
        print("This is an example task running in the Flask app context.")
        return "Task completed!"
    
@celery.task
def send_welcome_email(to_email):
    subject = 'Welcome to the Placement Portal'
    body = 'Thank you for registering on the Placement Portal.'
    
    with app.app_context():
        send_email(to_email, subject, body)