# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner

def creatsuite():
    testunit = unittest.TestSuite()
    #定义测试文件查询路径
    test_dir = r"F:\download\Pythontest\test_project\test_case"
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test*.py',
                                                   top_level_dir=None)

    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTests(test_case)
            print testunit
    return  testunit


if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    filename = "F:/download/Pythontest/test_project/report/" + u"测试报告正常" + ".html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例执行情况：")
    runner.run(creatsuite())