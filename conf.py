#coding=utf-8
import json
filename="C:\\Users\\Lenovo\\PycharmProjects\\FAMCAuto\\testData\\testData.xlsx"
def dict_ch_show(par):#字典转中文输出
    if type(par)==unicode:
        return json.dumps(json.loads(par),ensure_ascii=False, encoding='UTF-8')
    elif type(par)==dict:
        return json.dumps(par,ensure_ascii=False, encoding='UTF-8')
    elif type(par)==str:
        return json.dumps(eval(par),ensure_ascii=False, encoding='UTF-8')
    else:
        print('不能处理该字符串')

