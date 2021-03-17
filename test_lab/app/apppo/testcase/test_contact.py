# coding:utf-8
from up.test_lab.app.apppo.page.app import App


class TestContact:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardowm(self):
        self.app.stop()

    def test_addcontact(self):
        username = "张三9"
        mobilephone = "185111111110"
        editpage = self.main.goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(username, mobilephone)
        editpage.verify_ok()

    def test_deletecontact(self):
        username='张三2'
        delepage = self.main.goto_addresslist().goto_search().search_member(username).goto_edit().goto_delete()
        delepage.delete_contact()
        delepage.verify_ok()