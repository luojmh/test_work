from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.editcontact_page import EditContactPage


class PersonalPage(BasePage):
    def goto_edit(self):
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/igo").click()
        return EditContactPage(self.driver)