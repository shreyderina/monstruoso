class Config(object):

    config = None

    def __init__(self, path):
        self.config = open(path)

    def get_config(self):
        return self.config
