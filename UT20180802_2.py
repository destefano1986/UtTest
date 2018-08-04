# -*- coding: utf-8 -*-
import unittest

def fun(x):
    return x + 1

class Mytest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fun(3), 4)

    def test_2(self):
        self.assertNotEqual(fun(3), 5)

    def test_3(self):
        self.assertTrue(fun(3)==4)

    def test_4(self):
        self.assertFalse(fun(3)==5)

    '''
    places与delta不能同时存在，否则出异常
    若a==b，则直接输入正确，不判断下面的过程
    若delta有数，places为空，判断a与b的差的绝对值是否<=delta，满足则正确，否则错
    若delta为空，places有数，判断b与a的差的绝对值,取小数places位，等于0则正确，否则错误
    若delta为空，places为空，默认赋值places=7判断
    '''
    def test_5(self):
        self.assertAlmostEqual(fun(4),2,delta=4)

    def test_6(self):
        self.assertNotAlmostEqual(fun(4),10,delta=4)

    #判断a 与b的对象是否相同，不成立True，否则False
    def test_7(self):
        self.assertIsNot(fun(3), 5)

    def test_8(self):
        self.assertLess(fun(3), 5)

    def test_9(self):
        self.assertLessEqual(fun(3), 5)

    def test_10(self):
        self.assertGreater(fun(10), 5)

    def test_11(self):
        self.assertGreaterEqual(fun(10), 5)

    def test_12(self):
        self.assertIsInstance(fun(3),int)

    def test_13(self):
        self.assertIn(fun(3),[4,5,6])


if __name__ == '__main__':
    unittest.main()