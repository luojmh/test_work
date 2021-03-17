from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.delete_page import DeleteContactPage


class DeleteContactPage(BasePage):

    def goto_edit(self):
        self.findclick(MobileBy.XPATH, "//*[@text='编辑成员']")
        return DeleteContactPage(self.driver)




