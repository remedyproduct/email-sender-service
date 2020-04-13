import os
import requests
from senders.sender import Sender
import json


class MailgunSender(Sender):
    def __init__(self):
        self._base_mailgun_url = 'https://api.mailgun.net/v3'
        self._mailgun_api_key = os.environ['MAILGUN_API_KEY']
        self._mailgun_api_domain = os.environ['MAILGUN_API_DOMAIN']
        self._mailgun_url = f'{self._base_mailgun_url}/{self._mailgun_api_domain}/messages'
        self._email_sender = 'Ritual Media <postmaster@mailgun.ritual.io>'

    def _send_mail(self, template_name: str, recipient: str,
                   subject: str, context: dict):
        auth = ('api', self._mailgun_api_key)

        data = {
            'from': self._email_sender,
            'to': recipient,
            'subject': subject,
            'template': template_name,
            "h:X-Mailgun-Variables": json.dumps(context),
        }

        requests.post(self._mailgun_url,
                      auth=auth,
                      data=data)

    def send_confirm_email_message(self, recipient, code):
        template = "confirm_email"
        subject = "Ritual confirm email"
        context = {
            "otp_code": code
        }
        self._send_mail(template, recipient, subject, context)

    def send_reset_password_message(self, recipient, code):
        template = "reset_password"
        subject = "Ritual reset password"
        context = {
            "otp_code": code
        }
        self._send_mail(template, recipient, subject, context)
