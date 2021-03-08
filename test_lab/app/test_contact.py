# coding:utf-8
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

from selenium.common.exceptions import NoSuchElementException


class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["devicesName"] = "emulator-5554"
        # 获取appPackage和appActivity最佳命令
        # adb logcat ActivityManager:I | grep "cmp"

        # 企业微信
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        caps["skipServerInstallation"]: 'true'  # 跳过安装uiautomator2server等 服务
        caps["skipDeviceInitialization"]: 'true'  # 跳过设备的初始化
        caps["settings[waitForIdleTimeout]"]: 1   # settings 控制 动态页面的等待时长
        # caps['dontStopAppOnReset'] = "true"  # 运行前不停止app
        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardowm(self):
        self.driver.quit()
    def swipe_find(self,num,text):
        for i in range(num+1):
            if i==num:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找{num}次，未找到")
            self.driver.implicitly_wait(1)
            while True:
                try:
                    ele=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{text}']")
                    self.driver.implicitly_wait(5)
                    return ele
                except:
                    print("未找到")
                    size = self.driver.get_window_size()
                    width = size.get("width")
                    height = size.get("height")
                    start_x = width/2
                    start_y = height*0.8
                    end_x = start_x
                    end_y = height*0.3

                    self.driver.swipe(start_x,start_y,end_x,end_y,1000)

    def test_addcontact(self):
        '''
        完成企业添加联系人
        :return:
        '''
        username="zhangsan4"
        mobilephone=18611111115
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        element = self.swipe_find(3,"添加成员")
        element.click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(mobilephone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        assert toast == "添加成功"







