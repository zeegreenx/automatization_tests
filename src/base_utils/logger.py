
class Logger:
    def __init__(self, response):
        self.response = response

    def logs(self):
        return "\nINPUT DATA:\n"\
            f"\tReceived response code: {self.response.status_code}\n"\
            f"\tRequest url: {self.response.url}\n"
