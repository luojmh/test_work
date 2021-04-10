# coding:utf-8
import json
import requests

class TestAddress:

 # 查询用户信息
    def test_get_information(self):
        userid="m7800"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        r=requests.get(url)
        print(r.json())
 # 添加用户
    def test_create_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid":"m7800",
            "name":"aotaman0",
            "mobile":"18655555557",
            "department":1
        }
        r=requests.post(url,json=data)
        print(r.json())

    # 修改用户
    def test_update_member(self):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "m7800",
            "name": "aotaman1"
        }
        r=requests.post(url,json=data)
        print(r.json())

    # 删除用户
    def test_delete_member(self):
        userid="m7800"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        r=requests.get(url)
        print(r.json())
