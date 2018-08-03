#coding=utf-8
import unittest
from tools import HTMLTestRunner
import time
from unittest import TestLoader
#用例目录
test_suite_dir="C:\Users\Lenovo\PycharmProjects\FAMCAuto\\testCase\\"
report_dir="C:\Users\Lenovo\PycharmProjects\FAMCAuto\\report\\"
def creatsuite():
    testunit=unittest.TestSuite()
    test_dir=test_suite_dir#定义测试文件查找的目录
    #定义discover方法参数
    package_tests=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)
    #discover方法筛选出来的用例循环添加到测试套件中
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTest(test_case)
            #print(testunit)
    return testunit
alltestnames=creatsuite()
if __name__=="__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    test_report=report_dir
    filename=test_report+now+" result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u"FAMC测试报告",
                                         description=u"测试用例执行结果")
    runner.run(alltestnames)
    fp.close()

