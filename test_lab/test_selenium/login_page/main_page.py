# coding：utf-8
"""
按页面建类，按功能建函数
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from up.test_lab.test_selenium.login_page.login_page import LoginPage
from up.test_lab.test_selenium.login_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        self.driver.find_element(By.XPTH,"//a[@class='index_head_info_pCDownloadBtn']").click()
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPTH, "//a[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)