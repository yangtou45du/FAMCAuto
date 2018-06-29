#coding=utf-8
'''测试文件以test_开头（以_test结尾也可以）:全小写+下划线式驼峰
测试类以Test开头首字母大写式驼峰,example：ClassName()
测试函数以test_开头:全小写+下划线式驼峰
全局变量:全大写+下划线式驼峰 ,example：GLOBAL_VAR'''
import unittest
from unittest import TestCase
from common.send_request import SendRequest
import json
from ddt import ddt,data,unpack

testData=[{"url" :"http://221.236.20.217:8093/pcl/services/loanCenter/account/queryPaymentHistory","dict":{
    "params": {"loanNo": "000002017090601542","isPage": 1,"pageSize": "10","pageNo": "1"}}}]

@ddt
class LoanCenterInterfaceAPI(unittest.TestCase):
    def setUp(self):
        pass
    def sendRequest(self,url,dict,header=None):
        result = SendRequest().sendJsonRequests(url,dict,header)
        return json.dumps(json.loads(result)["meta"],ensure_ascii=False)#字典转中文输出
    @data(*testData)
    def test_loan_center_interface(self,data):
        result=self.sendRequest(data["url"],data["dict"])
        print result
if __name__=="__main__":
    unittest.main()