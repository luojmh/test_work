# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

from up.test_lab.test_selenium.address_page.address_page import AddressPage


class MainPage:
    def __init__(self):
        # 复用浏览器
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def goto_address(self):
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)

