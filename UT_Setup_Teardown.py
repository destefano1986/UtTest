# -*- coding: utf-8 -*-
import unittest

'''
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
'''
class TestDict(unittest.TestCase):

    def setUp(self):
        print ('setUp...')

    def tearDown(self):
        print ('tearDown...')


if __name__ == '__main__':
    unittest.main()