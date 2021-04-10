import pytest

from up.test_lab.test_requests.wework.WeworkAddress import WeworkAddress


class TestAddress:
    name="奥特曼"
    userid = "aotaman01"
    def setup_class(self):
        self.address = WeworkAddress()
        self.mobile="13701000000"
        self.department=[1]


    def setup(self):
        self.userid += "tmp"
        self.address.delete_member(self.userid)

    def teardown(self):
        self.address.delete_member(self.userid)

    def test_get_information(self):
        #数据处理
        self.address.create_member(self.userid,self.name,self.mobile,self.department)

        # 用户信息 是不是正确
        r=self.address.get_information(self.userid)
        assert r["name"]==self.name

    def test_create_member(self):
        r=self.address.create_member(self.userid,self.name,self.mobile,self.department)
        assert r.get("errmsg") == "created"
        info=self.address.get_information(self.userid)
        assert info["name"]==self.name

#参数化变量应该为类变量，不能为实例变量
    @pytest.mark.parametrize("userid,new_name",[("tmp",name+"tmp")]*2)
    def test_update_member(self,userid,new_name):
        userid = self.userid
        self.address.create_member(userid,self.name,self.mobile,self.department)
        # new_name = self.name + "tmp"
        r = self.address.update_member(userid,new_name)
        assert r.get("errmsg")=="updated"

        info = self.address.get_information(self.userid)
        assert info["name"]==new_name

    def test_delete_member(self):
        self.address.create_member(self.userid,self.name,self.mobile,self.department)
        r = self.address.delete_member(self.userid)
        assert r.get("errmsg")=="deleted"

        info = self.address.get_information(self.userid)
        assert info["errcode"] == 60111
