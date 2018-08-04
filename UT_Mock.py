# -*- coding: utf-8 -*-
'''
Mock 类库是一个专门用于在unittest过程中制作（伪造）和修改（篡改）测试对象的类库，制作和修改的目的是避免这些对象在单元测试过程中
依赖外部资源（网络资源，数据库连接，其它服务以及耗时过长等）。Mock是一个如此重要的类库，如果没有它，Unittest框架从功能上来说就是
不完整的。所以不能理解为何它没有出现在Python2的标准库里，不过我们可以很高兴地看到在Python3中mock已经是unittest框架的一部分。
'''
from unittest import mock
import unittest
from modular import Count

# test Count class
class TestCount(unittest.TestCase):
    def test_add(self):
        #首先，调用被测试类Count()
        count = Count()
        #通过Mock类模拟被调用的方法add()方法，return_value定义add()方法的返回值。
        count.add = mock.Mock(return_value=7)
        #接下来，相当于在正常的调用add()方法，传两个参数2和5，然后会得到相加的结果7。然后，7的结果是我们在上一步就预先设定好的
        result = count.add(2,5)
        #最后，通过assertEqual()方法断言，返回的结果是否是预期的结果7
        self.assertEqual(result,7)


if __name__ == '__main__':
    unittest.main()