import time
import requests
from celery import shared_task

@shared_task
def send_email_notification(user_email):
    print(f"Pochta jo'natish boshlandi: {user_email}")
    time.sleep(5)
    print(f"Pochta muvaffaqiyatli jo'natildi: {user_email}")
    return "OK"

@shared_task
def send_real_sms_task(phone_number, message_text):
    url = "https://eskiz.uz"
    payload = {
        "mobile_phone": phone_number,
        "message": message_text,
        "from": "4546"
    }
    headers = {
        "Authorization": "Bearer SIZNING_API_TOKENINGIZ_BUYERGA_YOZILADI"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.json()
