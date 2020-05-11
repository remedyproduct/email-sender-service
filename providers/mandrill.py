import os
import requests
import json
from providers.provider import Provider


class MandrillProvider(Provider):
    def __init__(self):
        self._mandrill_api_key = os.environ["MANDRILL_API_KEY"]
        self._mandrill_api_url = 'https://mandrillapp.com/api/1.0'
        self._mandrill_endpoint = f'{self._mandrill_api_url}/messages/send-template.json'

    def _send(self, template_name: str, recipient: str, context: dict):
        data = {
            'key': self._mandrill_api_key,
            'message': {
                'to': [{
                    'email': recipient
                }],
                'global_merge_vars': []
            },
            'template_name': template_name,
            'async': true
        }

        for key, value in context.items():
            data['message']['global_merge_vars'].append(
                {'name': key, 'content': value}
            )

        request.post(self._mandrill_endpoint, auth=None, data=data)

    def send_confirm_email_message(self, recipient, code):
        template = "confirm-email"
        context = {
            "otp_code": code
        }
        self._send(template, recipient, context)

    def send_reset_password_message(self, recipient, code):
        template = "reset-password"
        context = {
            "otp_code": code
        }
        self._send(template, recipient, context)
