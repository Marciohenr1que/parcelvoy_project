import requests
from celery import Celery

celery = Celery(__name__)

@celery.task
def send_reminder_email(api_key, to, subject, body):
    url = 'https://api.parcelvoy.com/v1/send'
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {
        'to': to,
        'subject': subject,
        'text': body
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()



