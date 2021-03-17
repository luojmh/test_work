# coding:utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import logging

# 基类，初始化driver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    logging.basicConfig(level=logging.WARNING)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def findclick(self, locator):
        logging.warning("findclick")
        logging.warning(f"{locator}")
        self.driver.find_element(MobileBy.XPATH, locator).click()

    def find_sendkeys(self, locator, value):
        logging.warning("find_sendkeys")
        logging.warning(f"{locator}, {value}")
        self.driver.find_element(MobileBy.XPATH, locator).send_keys(value)

    def swipe_find(self, num, text):

        for i in range(num + 1):
            if i == num:
                # logging.warning("set implicitly_wait:5")
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找{num}次，未找到")
            self.driver.implicitly_wait(1)
            while True:
                try:
                    ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                    self.driver.implicitly_wait(5)
                    return ele
                except:
                    print("未找到")
                    size = self.driver.get_window_size()
                    width = size.get("width")
                    height = size.get("height")
                    start_x = width / 2
                    start_y = height * 0.8
                    end_x = start_x
                    end_y = height * 0.3

                    self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
