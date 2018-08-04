# -*- coding: utf-8 -*-
'''
Mock 类库是一个专门用于在unittest过程中制作（伪造）和修改（篡改）测试对象的类库，制作和修改的目的是避免这些对象在单元测试过程中
依赖外部资源（网络资源，数据库连接，其它服务以及耗时过长等）。Mock是一个如此重要的类库，如果没有它，Unittest框架从功能上来说就是
不完整的。所以不能理解为何它没有出现在Python2的标准库里，不过我们可以很高兴地看到在Python3中mock已经是unittest框架的一部分。
'''
from unittest import mock
import unittest
from outer import add_and_multiply


class MyTestCase(unittest.TestCase):

    @mock.patch('outer.multiply')
    def test_add_and_multiply(self, mock_multiply):

        x = 3
        y = 5

        mock_multiply.return_value = 15

        addition, multiple = add_and_multiply(x, y)

        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

if __name__ == "__main__":
    unittest.main()