class TestClient(object):
    base_url = None

    def __init__(self):
        if self.base_url is None:
            raise Exception("define base_url")