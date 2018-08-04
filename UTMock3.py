# -*- coding: utf-8 -*-
from unittest import mock
import unittest


def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)
    return (addition, multiple)


def multiply(x, y):
    #return x * y
    return x * y + 3

'''
class MyTestCase(unittest.TestCase):
    def test_add_and_multiply(self):
        x = 3
        y = 5
        addition, multiple = add_and_multiply(x, y)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)
'''


class MyTestCase(unittest.TestCase):
    #patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试。
    # 在测试过程中，您指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原。
    @mock.patch("UTMock3.multiply")
    def test_add_and_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addition, multiple = add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()