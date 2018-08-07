#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import xlrd,sys
from openpyxl import load_workbook
from openpyxl import Workbook
import cx_Oracle
import json
from conf import *

def get_excel_dict( path, index=0):
    paralList=[]
    workbook=xlrd.open_workbook(path)#打开文件
    sheet=workbook.sheets()[index]#sheet索引从0开始
    firstRowDataList=sheet.row_values(0)#第一行数据
    #print firstRowDataList
    for rownum in range(1, sheet.nrows):#循环每一行数据
        list = sheet.row_values(rownum)
        dict={}
        dictTestCaseName={}
        for caseData in list:
            dict[firstRowDataList[list.index(caseData)]] =caseData.replace(" ", "") #每一行数据与第一行数据对应转为字典
            #json.dumps(json.loads(caseData), ensure_ascii=False)
        dictTestCaseName[list[2]]=dict#转为字典后与用例名字对应转为字典
        paralList.append(dictTestCaseName)#将处理后的数据放入列表里
    return (paralList)

#print get_excel_dict("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx")
def get_test_case_data(filename,testCaseName,index=0):
    testData = get_excel_dict(filename,index)
    getTestCaseDataList = []
    for data in testData:
        if (data.keys()[0]) == testCaseName:
            getTestCaseDataList.append(data[testCaseName])
    return getTestCaseDataList
if __name__=="__main__":
    testCaseName="test_loan_center_interface"
    print get_test_case_data(filename,testCaseName)
def get_api_url_dict( path, index=0):
    dict=[]
    workbook=xlrd.open_workbook(path)#打开文件
    sheet=workbook.sheets()[index]#sheet索引从0开始
    dict = {}
    for rownum in range(1, sheet.nrows):#循环每一行数据
        list = sheet.row_values(rownum)
        for caseData in list:
            dict[list[0].replace(" ","")] =list[1].replace(" ","")
    return (dict)

def get_dc(string):
    dc = {}
    if "\n" in string:
        list=string.split("\n")
        for i in list:
            if "=" in i:
                list1 = i.split("=")
                dc[list1[0].replace(" ","")] = list1[1].replace(" ","")
    else:
        if "=" in string:
            list1 = string.split("=")
            dc[list1[0].replace(" ","")] = list1[1].replace(" ","")

    return dc
def dict_ch_show(par):#字典转中文输出
    if type(par)==unicode:
        return json.dumps(json.loads(par),ensure_ascii=False, encoding='UTF-8')
    elif type(par)==dict:
        return json.dumps(par,ensure_ascii=False, encoding='UTF-8')
    elif type(par)==str:
        return json.dumps(eval(par),ensure_ascii=False, encoding='UTF-8')
    else:
        print('不能处理该字符串')

