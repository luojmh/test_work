from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from up.test_lab.app.apppo.page.addresslist_page import AddressListPage


class MainPage(BasePage):

    def goto_addresslist(self):
        # 解元组，放在变量中
        self.findclick("//*[@text='通讯录']")
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)