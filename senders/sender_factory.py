from senders.sender import Sender
from senders.mailgun_sender import MailgunSender
from senders.mandrill_sender import MandrillSender


class SenderFactory(object):
    def __init__(self, sender_name: str):
        self._senders = {
            "MAILGUN": MailgunSender,
            "MANDRILL": MandrillSender,
        }
        self._sender_class = self._senders[sender_name]

    def create_sender(self) -> Sender:
        sender = self._sender_class()
        return sender
