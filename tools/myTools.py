#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import xlrd,sys
from openpyxl import load_workbook
from openpyxl import Workbook
import cx_Oracle
import json

def get_excel_dict( path, index=0):
    paralList=[]
    workbook=xlrd.open_workbook(path)#打开文件
    sheet=workbook.sheets()[index]#sheet索引从0开始
    firstRowDataList=sheet.row_values(0)#第一行数据
    #print firstRowDataList
    for rownum in range(1, sheet.nrows):#循环每一行数据
        list = sheet.row_values(rownum)
        #print type(list[3])
        dict={}
        dictTestCaseName={}
        for caseData in list:
            dict[firstRowDataList[list.index(caseData)]] =caseData #每一行数据与第一行数据对应转为字典
            #json.dumps(json.loads(caseData), ensure_ascii=False)
        dictTestCaseName[list[2]]=dict#转为字典后与用例名字对应转为字典
        paralList.append(dictTestCaseName)#将处理后的数据放入列表里

    return (paralList)

#print get_excel_dict("C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx")
def get_test_case_data(filename,testCaseName,index=0):
    testData = get_excel_dict(filename,index)
    #print(testData)
    getTestCaseDataList = []
    for data in testData:
        if (data.keys()[0]) == testCaseName:
            getTestCaseDataList.append(data[testCaseName])
    return getTestCaseDataList
if __name__=="__main__":
    filename="C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx"
    testCaseName="test_loan_center_interface"
    print get_test_case_data(filename,testCaseName)

def write_log(msg):
    f=open("C:\\Users\\Lenovo\\PycharmProjects\\testdemo\\testdata\\log.txt","a")
    f.write(msg)
    f.close()
def write(list):
    filename="C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx"
    wb=load_workbook(filename)
    sheet = wb.active # 激活工作页
    sheet.append(list)
    wb.close()
    wb.save("C:\Users\Lenovo\PycharmProjects\\testdemo\\testdata\\test_result.xlsx")

def get_dc(string):
    list=string.split("\n")
    dc={}
    for i in list:
        list1=i.split("=")
        dc[list1[0]]=list1[1]
    return dc

