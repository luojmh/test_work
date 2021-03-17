from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from page.search_page import SearchPage
from up.test_lab.app.apppo.page.addcontact_page import AddContactPage


class AddressListPage(BasePage):

    def click_addcontact(self):
        element = self.swipe_find(3, "添加成员")
        element.click()
        return AddContactPage(self.driver)

    def goto_search(self):
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/igk").click()
        return SearchPage(self.driver)
