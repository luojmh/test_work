import requests
from wework.base import Base

class WeworkAddress(Base):

    # 查询用户信息
    def get_information(self,userid:str):
        parms={
            "userid":userid
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.send("GET",url,params=parms)
        return r.json()

    # 添加用户
    def create_member(self,userid,name,mobile,department:list):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send("POST",url, json=data)
        return r.json()

    # 修改用户
    def update_member(self,userid,name):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name
        }
        r = self.send("POST",url, json=data)
        return r.json()

    # 删除用户
    def delete_member(self,userid):
        params={
            "userid":userid
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = self.send("GET",url,params=params)
        return r.json()