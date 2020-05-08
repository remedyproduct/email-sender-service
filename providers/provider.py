class Provider(object):
    def send_confirm_email_message(self, recipient, code):
        raise NotImplementedError()

    def send_reset_password_message(self, recipient, code):
        raise NotImplementedError()
