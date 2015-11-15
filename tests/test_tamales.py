import unittest
from tamales import app, views


class TamalesUtilsTestCase(unittest.TestCase):
    def test_get_code(self):
        code = views.get_code('http://www.example.com')
        char_one = app.config['ALPHABET'][1]
        self.assertEqual(char_one, code)


class TamalesAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_basic(self):
        res = self.app.get('/api/v1/')
        self.assertEqual(res.status_code, 200)

    def test_unknown_code(self):
        res = self.app.get('/api/v1/urls/DoesNotExist')
        self.assertEqual(res.status_code, 404)
