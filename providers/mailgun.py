import os
import requests
import json
from providers.provider import Provider


class MailgunProvider(Provider):
    def __init__(self):
        self._mailgun_api_key = os.environ['MAILGUN_API_KEY']
        self._mailgun_api_domain = os.environ['MAILGUN_API_DOMAIN']
        self._email_provider = 'Ritual Media <postmaster@mailgun.ritual.io>'
        self._mailgun_api_url = 'https://api.mailgun.net/v3'
        self._mailgun_endpoint = f'{self._mailgun_api_url}/{self._mailgun_api_domain}/messages'

    def _send(self, template_name: str, recipient: str, subject: str, context: dict):
        auth = ('api', self._mailgun_api_key)
        data = {
            'from': self._email_provider,
            'to': recipient,
            'subject': subject,
            'template': template_name,
            "h:X-Mailgun-Variables": json.dumps(context),
        }

        requests.post(self._mailgun_endpoint, auth=auth, data=data)

    def send_confirm_email_message(self, recipient, code):
        template = "confirm_email"
        subject = "Ritual: Confirm email"
        context = {
            "otp_code": code
        }
        self._send(template, recipient, subject, context)

    def send_reset_password_message(self, recipient, code):
        template = "reset_password"
        subject = "Ritual reset password"
        context = {
            "otp_code": code
        }
        self._send(template, recipient, subject, context)
