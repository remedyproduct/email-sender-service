import os
from provider_factory import ProviderFactory

APP_NAME = os.getenv("APP_NAME", )
PROVIDER = os.getenv("PROVIDER", "MAILGUN")

provider_factory = ProviderFactory(PROVIDER)
provider = provider_factory.create_provider()


def send_confirmation_email(recipient, code):
    provider.send_confirm_email_message(recipient, code)


def send_reset_password_code(recipient, code):
    provider.send_reset_password_message(recipient, code)
