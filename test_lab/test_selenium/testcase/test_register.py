# coding:utf-8

import time
from up.test_lab.test_selenium.login_page.main_page import MainPage


class TestRegister:
    def test_register(self):
        main = MainPage()
        main.goto_register().register()
        time.sleep(6)

    def test_login_register(self):
        main=MainPage()
        main.goto_login().goto_register()

