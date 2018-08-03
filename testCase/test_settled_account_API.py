#coding=utf-8#
import time
import json
from common.send_request import SendRequest
from ddt import ddt,data,unpack
import unittest
from unittest import TestCase
from tools.myTools import *
test_settled_account_list = get_test_case_data("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx","test_settled_account",1)
@ddt
class TestSettledAccountAPI(unittest.TestCase):
    def setUp(self):
        pass
    def __send_request__(self,url,dict,header):
        re=SendRequest().sendJsonRequests(url,dict,header)
        result=json.dumps(json.loads(re), ensure_ascii=False, encoding='UTF-8')#将unicode转为字典
        return result
    @data(*test_settled_account_list)
    @unittest.skip(" skip test settled account")
    def test_settled_account(self,data):
        header=get_dc(data['header'].encode('utf-8'))
        try:
            result=self.__send_request__(data["url"], json.loads(data["paral"]),header)
            exception = json.dumps(json.loads(data["except"]), ensure_ascii=False, encoding='UTF-8')  # 处理字典中文输出显示
            results = json.dumps(json.loads(result), ensure_ascii=False, encoding='UTF-8')  # 处理字典中文输出显示
            self.assertEqual(exception, results)
        except Exception as err:
            self.assertIn('ConnectionError', repr(err)[:15])



if __name__=="__main__":
   unittest.main()

