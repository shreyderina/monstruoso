from human_curl import request

from .response import ResponseWrapper


class ResponseChecker(object):
    def __init__(self, checker, response):
        self.checker = checker
        self.response = response

    def __enter__(self):
        if self.checker is not None:
            self.checker(self.response)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            result = 'FAIL'
        else:
            pass


class Method(object):

    _response_type = None
    _response_checker = None

    def __init__(self, test_client, uri, handlers=None, response_checker=None):
        self.test_client = test_client
        self.uri = uri
        self.handlers = handlers if handlers is not None else {}
        self._response_checker = response_checker

    def add_response_handler(self, handler):
        self.handlers = dict(self.handlers.items() + handler.items())
        return self

    def response_type(self, response_type):
        self._response_type = response_type
        return self

    def after_response(self, checker=None):
        self._response_checker = checker
        return self

    def request(self, method, params=None, response_type=None):
        if response_type is not None and response_type in self.handlers.keys():
            handler = self.handlers[response_type]
        elif self._response_type is not None and self._response_type in self.handlers.keys():
            handler = self.handlers[self._response_type]
        else:
            handler = ResponseWrapper
        url = self.test_client.base_url + self.uri
        response = handler(request(method=method, url=url, params=params))

        with ResponseChecker(self._response_checker, response):
            return response