# coding:utf-8
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.personal_page import PersonalPage
from time import sleep


class SearchPage(BasePage):
    def search_member(self,username):
        self.find_sendkeys("//*[@text='搜索']", username)
        print("-----debug","//*[@text='{}']".format(username))
        sleep(3)
        ele=self.driver.find_elements(MobileBy.XPATH,"//*[@text='{}']".format(username))
        print("元素个数",ele)
        if len(ele) > 1:
            ele[1].click()
        return PersonalPage(self.driver)



