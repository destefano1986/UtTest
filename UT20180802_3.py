# -*- coding: utf-8 -*-
import unittest


def raisesIOError(*args, **kwds):
    raise IOError("TestIOError")


class FixtureTest(unittest.TestCase):
    def test1(self):
        self.assertRaises(IOError, raisesIOError)


if __name__ == '__main__':
    unittest.main()