import tamales
import unittest


class TamalesUtilsTestCase(unittest.TestCase):
    def test_generate_code(self):
        code = tamales.generate_code()
        self.assertEqual('aa', code)


class TamalesAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = tamales.app.test_client()

    def test_simple(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
