#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import mock
import unittest
import requests

class Count():
    def add(self, a, b):
        return a + b

# test Count class
class TestCount(unittest.TestCase):
    def test_add(self):
        count = Count()
        #side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。
        # 简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。
        #count.add = mock.Mock(return_value=13)
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 8)
        #count.add.assert_called_with(8, 8)
        self.assertEqual(result, 16)

if __name__=="__main__":
    unittest.main()