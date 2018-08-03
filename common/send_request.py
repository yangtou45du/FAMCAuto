
import requests
import json
class SendRequest():
    def sendJsonRequests(self,url,dict,header=None):
        re=requests.post(url,json=dict,headers=header)
        return re.text
    def sendDataRequests(self,url,dict,header=None):
        re=requests.post(url,data=dict,headers=header)
        return re.text

if __name__ == '__main__':
    url = "http://221.236.20.227:8090/credit_api/open/data/v3.0/FS016/weChatData "
    dict ={


    "reqFrom":"CMS",
    "taskId":"bgpfI4PEjoG600R10",
    "reqMark":"64126197802052335"
}
    f = SendRequest().sendJsonRequests(url, dict)
    print f

