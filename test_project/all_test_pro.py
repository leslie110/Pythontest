# -*- coding:utf-8 -*-
import HTMLTestRunner
import unittest,time,os,multiprocessing

#查找多个含有thread的文件夹，文件
def EEEcreatsuit():
    casedir = []
    listaa = os.listdir(r'F:\download\Pythontest\test_project')
    for xx in listaa:
        if "thread" in xx:
            casedir.append(xx)
    suit = []
    for n in casedir:
        testsuit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(n,
                                                       pattern="test*.py",
                                                       top_level_dir=n)
        print discover
        for test_suit in discover:
            for test_case in test_suit:
                testsuit.addTest(test_case)
        suit.append(testsuit)
    print "===casedir===",casedir
    print "++++++++++++++++++++++++++++++++++++++++"
    print "!!!suit:!!!",suit
    return suit,casedir

#多线程运行测试套件，将结果写入HTMLTestRunner报告中
def EEEEmultiRunCase(suit,casedir):
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = r'F:\download\Pythontest\test_project\report/'+now+'result.html'
    fp = file(filename,'wb')
    fp.close()
    proclist = []
    s=0
    for i in suit:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'测试报告',
                                               description=u"用例执行情况")
        proc = multiprocessing.Process(target=runner.run,args=(i, ))
        proclist.append(proc)
        s=s+1
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()

if __name__=="__main__":
    runtmp = EEEcreatsuit()
    EEEEmultiRunCase(runtmp[0],runtmp[1])

