# coding:utf-8
from up.test_lab.test_selenium.address_page.main_page import MainPage


class TestAddress:
    def test_add_menber(self):
        main=MainPage()
        main.goto_address().add_member()
