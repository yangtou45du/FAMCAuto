#coding=utf-8#
import time
import json
from common.send_request import SendRequest
from ddt import ddt,data,unpack
import unittest
from unittest import TestCase
from tools.myTools import *
from conf import *
test_settled_account_list = get_test_case_data(filename,"test_settled_account",2)
@ddt
class TestSettledAccountAPI(unittest.TestCase):
    def setUp(self):
        pass
    def __send_request__(self,url,dict,header):
        re=SendRequest().sendJsonRequests(url,dict,header)
        result=dict_ch_show(re)#将unicode转为字典
        return result
    @data(*test_settled_account_list)
    @unittest.skip(" skip test settled account")
    def test_settled_account(self,data):
        api_url = get_api_url_dict(filename)
        url = api_url[data['APIName']] + data["url"]
        header=get_dc(data['header'].encode('utf-8'))
        try:
            result=self.__send_request__(url, json.loads(data["paral"]),header)
            exception = dict_ch_show(data["except"])  # 处理字典中文输出显示
            results =dict_ch_show(result)  # 处理字典中文输出显示
            self.assertEqual(exception, results)
        except Exception as err:
            self.assertIn('ConnectionError', repr(err)[:15])



if __name__=="__main__":
   unittest.main()

