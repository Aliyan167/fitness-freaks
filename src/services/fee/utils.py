from twilio.rest import Client
from django.conf import settings

def send_whatsapp_message(to_number, message):
    # Twilio credentials (store these in your settings.py)
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    from_whatsapp_number = 'whatsapp:03118824647'  # Your Twilio WhatsApp number

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=f'whatsapp:{to_number}'
    )

    return message.sid
