# coding:utf-8
import ddt
import unittest
'''
# 测试数据
test_data1 = [{"username": "zhangsan", "pwd": "zhangsan"},
              {"username": "lisi", "pwd": "lisi"},
              {"username": "wangwu", "pwd": "wangwu"},
              ]
test_data2 = [{"username": "wukong", "pwd": "wukong"},
              {"username": "wuneng", "pwd": "woneng"},
              {"username": "wujing", "pwd": "wujing"},
              ]


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("Start!")

    def tearDown(self):
        print("end!")

    @ddt.data(*test_data1)
    def test_ddt1(self, data):
        print(data)

    @ddt.data(*test_data2)
    def test_ddt2(self, data):
        print(type(data))
        '''
from tools.myTools import *
testData = getExcelDict("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx")
print(type(testData))