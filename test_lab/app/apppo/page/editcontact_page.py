from appium.webdriver.common.mobileby import MobileBy
from page.delete_page import DeleteContactPage
from page.base_page import BasePage


class EditContactPage(BasePage):
    """
    手动输入添加成员页面
    """

    def edit_contact(self, username, mobilephone):
        self.find_sendkeys('//*[contains(@text,"姓名")]/..//*[@text="必填"]',username)
        self.find_sendkeys('//*[contains(@text,"手机")]/..//*[@text="必填"]',mobilephone)
        self.findclick('//*[@text="保存"]')

    def verify_ok(self):
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        assert toast == "添加成功"

    def goto_delete(self):
        self.findclick("//*[@text='编辑成员']")
        return DeleteContactPage(self.driver)
