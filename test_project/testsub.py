# -*- coding:utf-8 -*-
import unittest
from bayue.count import Count
class Test_jianfa(unittest.TestCase):#减法运算测试

    def setUp(self):
        pass
    #计算整数相减
    def test_jianfa(self):
        self.j = Count(8,5)
        self.jianfa = self.j.jianfa()
        self.assertEqual(self.jianfa,3)

    #计算小数相减
    def test_jianfa1(self):
        self.j = Count(10.2,5.3)
        self.jianfa = round(self.j.jianfa(),1)
        self.assertEqual(self.jianfa,4.9)

    def tearDown(self):
        pass



if __name__ == "__main__":
    #构造测试集
    suite = unittest.TextTestRunner
    suite.addTest(Test_jianfa("test_jianfa"))
    suite.addTest(Test_jianfa("test_jianfa1"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)