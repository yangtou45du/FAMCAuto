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
import unittest
from unittest import TestCase
from common.send_request import SendRequest
import json
from ddt import ddt,data,unpack
from tools.myTools import *
test_settled_account_list = get_test_case_data("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx","test_settled_account",1)
@ddt
class LoanCenterInterfaceAPI(unittest.TestCase):
    def setUp(self):
        pass
    def __sendRequest__(self,url,dict,header=None):
        result = SendRequest().sendJsonRequests(url,dict,header)
        return json.dumps(json.loads(result)["meta"],ensure_ascii=False)#字典转中文输出
    @data(*test_loan_center_interface_data)
    def test_loan_center_interface(self,data):
        try:
            if data["paral"]=="" or data["paral"].encode("utf-8").isspace():
                result = self.__sendRequest__(data["url"], " ")
            else:
                result = self.__sendRequest__(data["url"], json.loads(data["paral"]))
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
    

    url="http://221.236.20.215:802/ams/out/api/queryLoanTypeByLoanNo"
    dict= {
        "params":{
        "loanNo":"100002018071600610",
        "systemFlag":"f0001"
        }
        }
    header={'action':"com.hansy.forsaler.action.ForSalerAction",'method':"queryLoanTypeByLoanNo"}
    f=TestSettledAccountAPI().test_settled_account(url,dict,header)

'''

