from human_curl import Response
import json


class ResponseWrapper(Response):

    def __init__(self, wrapped_response):
        """
        :type wrapped_response: CurlResponse
        """
        self.wrapped_response = wrapped_response
        self.__dict__.update(wrapped_response.__dict__)


class JsonResponse(ResponseWrapper):
    @property
    def content_as_dict(self):
        return dict(json.loads(self.content))


class XmlResponse(ResponseWrapper):
    @property
    def content_as_dict(self):
        pass