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
import requests, unittest


class Test(unittest.TestCase):
    '''
    智能办单验证码
    '''

    def test01(self):
        url = "http://112.45.122.19:8092/sms_web/api/add/send/ZNBD_CODE/12020063"

        payload = 'dataParams=[{"table_key":"test000166","mobile":"13558700173","context":"手机验证码是：866322。1分钟内有效。","delay":0}]'
        header = {
            'content-type': "application/x-www-form-urlencoded",
            'charset' : "utf8",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=header)
        #result = response.json()
        #print(result)


# coding=utf-8#
import time
import json
from common.send_request import SendRequest
from ddt import ddt, data, unpack
import unittest
from unittest import TestCase
from tools.myTools import *
from tools.connectOracle import connectOracle
import random

test_wms_sms_list = get_test_case_data("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx",
                                       "test_wms_sms", 2)


@ddt
class TestWmsSmsAPI(unittest.TestCase):
    def setUp(self):
        pass

    def __send_request__(self, url, dict, header):
        re = SendRequest().sendDataRequests(url, dict, header)
        result = json.dumps(json.loads(re), ensure_ascii=False, encoding='UTF-8')  # 将unicode转为字典
        return result

    @data(*test_wms_sms_list)
    # @unittest.skip(" skip test settled account")
    def test_wms_sms(self, data):
        # print type(data["sql"].encode('UTF-8'))
        # sql="select * from (select tb.*, rownum from T_SMSPLTFORM_SNED_DATA tb where tb.applic_code = '"+data["APIDescribe"].encode('utf-8')+"' order by tb.busi_dt desc )where rownum=1"
        # print(sql)
        context_demo = connectOracle("wms_pro").sqlSelect(data["sql"].encode('UTF-8'))
        context = (context_demo[0][2]).decode('gbk')
        # print (context).decode('gbk')
        header = get_dc(data['header'].encode('utf-8'))
        print(header)
        pa = (data["paral"].encode('utf-8')).split('"context":"')
        payload = pa[0] + "\"context\":\"" + (context) + pa[1]
        print(payload)
        print type(payload)
        #result1 = self.__send_request__(data["url"], payload, header)
        #print(result1)
        print(222)
        result1 = self.__send_request__(data["url"], payload.encode('utf-8'), header)
        print(1111)
        exception = eval(data["except"])[0]  # 将字符串转为列表
        print (exception)
        result = eval(result1)[0]  # 处理字典中文输出显示
        print(result)
        print (result["data"]['table_key'])
        key = []
        print(3)
        for exception_key in exception.keys():
            key.append(exception_key)
        print(key)

        if result["data"]['context'] == context and len(result["data"]['data_code']) == 32 and len(result["data"]['dep_id']) == 32:
            for i in key:
                print type(exception["data"][i].encode('utf-8'))
                print 121
                print type(result["data"][i].encode('utf-8'))
                self.assertEqual(exception["data"][i], result["data"][i])
        else:
            self.assertEqual(1, 2)
        self.assertEqual(exception['code'], result["code"])
'''
        try:
            result1 = self.__send_request__(data["url"], payload, header)
            print(2)
            exception = eval(data["except"])[0]  # 将字符串转为列表
            print(exception)
            result = eval(result1)[0]  # 处理字典中文输出显示
            print(result)
            key = []
            print(3)
            for exception_key in exception.keys():
                key.append(exception_key)
            print(key)
            if result['context'] == context and len(result['data_code']) == 32 and len(result['dep_id']) == 32:
                for i in key:
                    self.assertEqual(exception["data"][i], result["data"][i])
            self.assertEqual(exception['code'], result["code"])
        except Exception as err:
            pass
            # self.assertIn('ConnectionError', repr(err)[:15])

    
        '''


if __name__ == "__main__":
    unittest.main()




