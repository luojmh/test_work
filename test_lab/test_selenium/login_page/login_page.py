# coding:utf-8
# @Time:2021/2/27

import json
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from up.test_lab.test_selenium.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.XPATH,"//a[@class='login_registerBar_link']").click()
        RegisterPage(self.driver)




