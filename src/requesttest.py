import requests
import json
class requesttest():
    def get(self,url,params,headers):
        try:
            r=requests.get(url,params=params,headers=headers)
            print("get请求获取响应状态码=", r.status_code)
            print("get请求获取响应头=", r.headers)
            print("get请求的响应结果（json）=", r.text)
            json_r = r.json()
            print("请求返回的响应结果（python类型）为：", json_r)
            return json_r
        except Exception as e:
            print("请求异常：", str(e))

    def post_json(self,url,data,headers):
        try:
            data=json.dumps(data)#将数据转换为json类型,是dumps，不是dump
            print("转换json后的数据",data)
            r=requests.post(url,data=data,headers=headers)#json格式
            print("获取响应状态码=",r.status_code)
            print("获取响应头",r.headers)
            json_r=r.json()
            print("请求返回的响应结果为：", json_r)
            return json_r
        except Exception as e:
            print("请求异常：",str(e))

    def post_form(self, url, data, headers):
        try:
            r=requests.post(url,data=data,headers=headers)#表单格式
            json_r=r.json()#转换为python类型
            print("请求返回的响应结果为：", json_r)
            return json_r
        except Exception as e:
            print("请求异常：",str(e))

'''
#调试
url="http://v.juhe.cn/laohuangli/d"
params={"key":"e711bc6362b3179f5a28de7fd3ee4ace","date":"2014-09-09"}
headers={}
re=requesttest()
re.post_json(url,params,headers)
'''