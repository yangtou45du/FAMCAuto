
import requests
import json
class SendRequest():
    def sendJsonRequests(self,url,dic,header=None):
        re=requests.post(url,json=dict,headers=header)
        return re.text
    def sendDataRequests(self,url,dict,header=None):
        re=requests.post(url,data=dict,headers=header)
        return re.text




if __name__ == '__main__':
    url = "http://221.236.20.217:8093/pcl/services/loanCenter/account/queryPaymentHistory"
    dict = {
        "params": {
            "loanNo": "000002017090601542",
            "isPage": 1,
            "pageSize": "10",
            "pageNo": "1"
        }
    }
    f = SendRequest().sendJsonRequests(url, dict)
    print f

