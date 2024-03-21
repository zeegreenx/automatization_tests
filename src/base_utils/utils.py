# from src.enums.global_enums import GlobalErrorMessages
from src.base_utils.logger import Logger


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.status_code = response.status_code
        self.logger = Logger(response)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.status_code in status_code, self
        else:
            assert self.status_code == status_code, self
            return self

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema(item)
            else:
                schema(self.response_json)
            return self

    def __str__(self):
        return \
            f"{self.logger.logs()}"f"\tResponse body: {self.response_json}\n"


class DelResponse:
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        self.logger = Logger(response)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.status_code in status_code, self
        else:
            assert self.status_code == status_code, self
            return self, status_code

    def __str__(self):
        return self.logger.logs()


class DelayedResponse(Response):
    def __init__(self, response, received_delay: float, expected_delay: float):
        super().__init__(response)
        self.logger = Logger(response)
        self.received_delay = received_delay
        self.expected_delay = expected_delay

    def assert_compare_delay(self):
        assert self.expected_delay == self.received_delay, self

    def __str__(self):
        delay_message = "Delay information not available."
        if self.received_delay is not None and self.expected_delay is not None:
            delay_message = f"The request returned with incorrect delay, expected at least {self.expected_delay} seconds, received {self.received_delay}."
        return self.logger.logs() + delay_message
