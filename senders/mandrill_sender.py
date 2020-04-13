import os
import mandrill
from senders.sender import Sender


class MandrillSender(Sender):
    def __init__(self):
        mandrill_api_key = os.environ["MANDRILL_API_KEY"]
        self._mandrill_client = mandrill.Mandrill(mandrill_api_key)

    def _send_mail(self, template_name: str, recipient: str, context: dict):
        message = {
            'to': [],
            'global_merge_vars': []
        }

        message['to'].append({'email': recipient})

        for key, value in context.items():
            message['global_merge_vars'].append(
                {'name': key, 'content': value}
            )

        self._mandrill_client.messages.send_template(template_name, [], message)

    def send_confirm_email_message(self, recipient, code):
        template = "confirm-email"
        context = {
            "otp_code": code
        }
        self._send_mail(template, recipient, context)

    def send_reset_password_message(self, recipient, code):
        template = "reset-password"
        context = {
            "otp_code": code
        }
        self._send_mail(template, recipient, context)
