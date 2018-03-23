# -*- coding:utf-8 -*-
from bayue.count import Count
import unittest

class Test_count(unittest.TestCase):#加法运算测试

    def setUp(self):
        pass
    #调试整数相加
    def test_add(self):
        self.j = Count(2,3)
        self.add = self.j.add()
        self.assertEqual(self.add,5)
    #调试小数相加
    def test_add1(self):
        self.j = Count(2.3,3.4)
        self.add = round(self.j.add(),1)
        self.assertEqual(self.add,5.7)

    #测试字符串相加

    def test_add2(self):
        self.j = Count("hello","world")
        self.add = self.j.add()
        self.assertEqual(self.add,"helloworld")

    def tearDown(self):
        pass

if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Test_count("test_add"))
    suite.addTest(Test_count("test_add1"))
    suite.addTest(Test_count("test_add2"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)