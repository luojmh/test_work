# coding:utf-8
import json
import requests

class TestAddress:
    def setup(self):
        self.token=self.get_token()

    def get_token(self):
        corpid="ww29f69b6f59aceec8"
        corpsecret="KVl_yvLhGHXVEv3HX4y0nrznStVX_LDtuUCM79DFfJQ"
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        return r.json()["access_token"]
 # 查询用户信息
    def test_get_information(self):
        userid="LuoJunMei"
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
