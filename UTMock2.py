from unittest import mock
import unittest

class Count():
    def ad(self):
        pass

class MockDemo(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.ad = mock.Mock(return_value=13)
        self.assertEqual(count.ad(), 13)

if __name__ == '__main__':
    unittest.main()

