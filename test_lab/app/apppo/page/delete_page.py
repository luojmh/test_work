from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from time import sleep

class DeleteContactPage(BasePage):
    def delete_contact(self):
        self.findclick("//*[@text='删除成员']")
        self.findclick("//*[@text='确定']")

    def verify_ok(self):
        sleep(5)
        self.driver.find_element("//*[@text='无搜索结果']")