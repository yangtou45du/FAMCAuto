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
from tools.myTools import *
test_loan_center_interface_list = get_test_case_data("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx","test_loan_center_interface")
@ddt
class LoanCenterInterfaceAPI(unittest.TestCase):
    def setUp(self):
        pass
    def __sendRequest__(self,url,dict,header=None):
        result = SendRequest().sendJsonRequests(url,dict,header)
        return json.dumps(json.loads(result)["meta"],ensure_ascii=False)#字典转中文输出
    @data(*test_loan_center_interface_list)
    def test_loan_center_interface(self,data):
        try:
            if data["paral"]=="" or data["paral"].encode("utf-8").isspace():
                result = self.__sendRequest__(data["url"], " ")
            else:
                result = self.__sendRequest__(data["url"], json.loads(data["paral"]))
                print(type(data["url"]))
            exception=json.dumps(json.loads(data["except"]), ensure_ascii=False, encoding='UTF-8')#处理字典中文输出显示
            results=json.dumps(json.loads(result), ensure_ascii=False, encoding='UTF-8')#处理字典中文输出显示
            self.assertEqual(exception,results)
        except Exception as err:
            self.assertIn('ConnectionError', repr(err)[:15])




if __name__=="__main__":
    unittest.main()
    '''
    suite=unittest.TestSuite()
    suite.addTest(LoanCenterInterfaceAPI("test_loan_center_interface"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
    '''
