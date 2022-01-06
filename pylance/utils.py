from twilio.rest import Client
import os
from django.db import models

account_sid = 'AC1db9fb1ee7fa1fda0289355b5a5f73b0'
auth_token = '3b9e42ccd3b39be2859fbdc3bfdd47b3'
client = Client(account_sid, auth_token)

def send_sms(user_code,phone_number):
            message = client.messages \
                            .create(
                                body=f"The current result is bad - {user_code}",
                                from_='+13185269439',
                                to=f"{phone_number}"
                            )

            print(message.sid)
