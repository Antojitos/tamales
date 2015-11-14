import tamales
import unittest


class TamalesUtilsTestCase(unittest.TestCase):
    def test_get_code(self):
        code = tamales.get_code('http://www.example.com')
        char_one = tamales.app.config['ALPHABET'][1]
        self.assertEqual(char_one, code)


class TamalesAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = tamales.app.test_client()

    def test_simple(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
