import urllib
import human_curl as requests
from human_curl import Response as CurlResponse


class RequestPart(object):

    def __init__(self, string=''):
        super(RequestPart, self).__init__()
        self.string = string


class BasePart(object):

    def __init__(self, base_url):
        super(BasePart, self).__init__()
        self.base_url = base_url


class Response(CurlResponse):

    def __init__(self, wrapped_response):
        """
        :type wrapped_response: CurlResponse
        """
        self.wrapped_response = wrapped_response
        self.__dict__.update(wrapped_response.__dict__)

    def __getattr__(self, attr):
        orig_attr = self.wrapped_response.__getattribute__(attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                result = orig_attr(*args, **kwargs)
                # prevent wrapped_class from becoming unwrapped
                if result == self.wrapped_response:
                    return self
                return result
            return hooked
        else:
            return orig_attr


def form_request(function):
    def wrapper(*args, **kwarg):
        uri = function(*args, **kwarg) + "/?" + urllib.urlencode(args[1])
        return uri

    return wrapper


def make_get_request(function):
    def wrapper(*args, **kwarg):
        request = function(*args, **kwarg)
        response = requests.get(request)
        return response

    return wrapper


def get_request(request):
    print request
    response = requests.get(request)
    return response