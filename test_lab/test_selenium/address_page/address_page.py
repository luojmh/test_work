# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver=driver

    def add_member(self):
        def wait_name(driver):
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            eles[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)

        # 输入姓名
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("name1")
        # 输入账号
        self.driver.find_element(By.XPATH, "//input[@id='memberAdd_acctid']").send_keys("account1")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//input[@id='memberAdd_phone']").send_keys("13910844999")
        # 点击保存
        self.driver.find_element(By.XPATH, "(//*[@class='qui_btn ww_btn js_btn_save'])[1]").click()