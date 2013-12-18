import unittest


class TestCase(unittest.TestCase):
    def __init__(self, *arg, **kwargs):
        super(TestCase, self).__init__(*arg, **kwargs)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
