# -*- coding:utf-8 -*-
import unittest

#加载测试文件
import testadd
import testsub

#构造参数集
suite = unittest.TestSuite()
suite.addTest(testadd.Test_count("test_add"))
suite.addTest(testadd.Test_count("test_add1"))
suite.addTest(testadd.Test_count("test_add2"))
suite.addTest(testsub.Test_jianfa("test_jianfa"))
suite.addTest(testsub.Test_jianfa("test_jianfa1"))

    #执行测试
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)