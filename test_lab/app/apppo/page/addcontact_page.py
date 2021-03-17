from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from up.test_lab.app.apppo.page.editcontact_page import EditContactPage
from time import sleep


class AddContactPage(BasePage):

    def addcontact_menual(self):
       # 手动输入添加
        self.findclick("//*[@text='手动输入添加']")
        sleep(3)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)
