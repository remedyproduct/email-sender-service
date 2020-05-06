from providers.provider import Provider
from providers.mailgun import MailgunProvider
from providers.mandrill import MandrillProvider


class ProviderFactory(object):
    def __init__(self, provider_name: str):
        self._providers = {
            "MAILGUN": MailgunProvider,
            "MANDRILL": MandrillProvider,
        }
        self._provider_class = self._providers[provider_name]

    def create_provider(self) -> Provider:
        provider = self._provider_class()
        return provider
