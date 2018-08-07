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
#from tools.myTools import *
#testData = getExcelDict("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx")
#print(type(testData))


#coding=utf-8
'''测试文件以test_开头（以_test结尾也可以）:全小写+下划线式驼峰
测试类以Test开头首字母大写式驼峰,example：ClassName()
测试函数以test_开头:全小写+下划线式驼峰
全局变量:全大写+下划线式驼峰 ,example：GLOBAL_VAR'''

#coding=utf-8
import requests, unittest,json
from conf import *
from tools.myTools import *
url="http://221.236.20.217:8093/pcl/services/loanCenter/account/queryPaymentDetails"
dict={
    "params": {
        "loanNo": "",
        "isPage":1,
        "pageSize":"10",
        "pageNo":"1"
    }
}
#result =requests.post(url, json=dict)
#print dict_ch_show(json.loads(result.text)["meta"])

#print json.dumps(json.loads(result)["meta"], ensure_ascii=False)  # 字典转中文输出
list=["   dd",2,3]
for i in range(len(list)):
    list[i]=str(list[i]).replace(" ","")
print(list)