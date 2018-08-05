#coding=utf-8#
import time
import json
from common.send_request import SendRequest
from ddt import ddt,data,unpack
import unittest
from unittest import TestCase
from tools.myTools import *
from tools.connectOracle import connectOracle
import random
test_wms_sms_list = get_test_case_data("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx","test_wms_sms",2)
@ddt
class TestWmsSmsAPI(unittest.TestCase):
    def setUp(self):
        pass
    def __send_request__(self,url,dict,header):
        re=SendRequest().sendDataRequests(url,dict,header)
        result=json.dumps(json.loads(re), ensure_ascii=False, encoding='UTF-8')#将unicode转为字典
        return result
    @data(*test_wms_sms_list)
    @unittest.skip(" skip test wms sms")
    def test_wms_sms(self,data):
        context_demo = connectOracle("wms_pro").sqlSelect(data["sql"].encode('UTF-8'))
        context=(context_demo[0][2]).decode('gbk')
        header=get_dc(data['header'].encode('utf-8'))
        pa=(data["paral"].encode('utf-8')).split('"context":"')
        payload=pa[0]+"\"context\":\""+(context)+pa[1]
        try:
            result1 = self.__send_request__(data["url"], payload.encode('utf-8'), header)
            exception =eval(data["except"])[0] # 将字符串转为列表
            print(exception)
            result = eval(result1)[0]  # 处理字典中文输出显示
            print(result)
            print type(result["data"]['context'])
            print(type(context))
            key = []
            print(3)
            for exception_key in exception.keys():
                key.append(exception_key)
            print(key)
            if result["data"]['context'] == context.encode('utf-8') and len(result["data"]['data_code']) == 32 and len(result["data"]['dep_id']) == 32:
                for i in key:
                    self.assertEqual(exception["data"][i],result["data"][i])
            else:
                self.assertEqual(1,2)
            #print(exception['code'])
            #print type(exception['code'])
            #print(result["code"])
            #print type(result["code"])
            #self.assertEqual(exception['code'],result["code"])
        except Exception as err:
            self.assertIn('ConnectionError', repr(err)[:15])
if __name__ == "__main__":
    unittest.main()


