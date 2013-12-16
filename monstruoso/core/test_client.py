from human_curl import Response as CurlResponse
from human_curl import get, post


class TestClient(object):
    def __init__(self, url):
        self.url = url