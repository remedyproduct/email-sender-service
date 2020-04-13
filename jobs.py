import os
from senders.sender_factory import SenderFactory


MAIL_SENDER = os.getenv("MAIL_SENDER", "MAILGUN")

sender_factory = SenderFactory(MAIL_SENDER)
sender = sender_factory.create_sender()


def send_confirmation_email(recipient, code):
    sender.send_confirm_email_message(recipient, code)


def send_reset_password_code(recipient, code):
    sender.send_reset_password_message(recipient, code)
