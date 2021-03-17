
# 启动app，停止app，重启app
from appium import webdriver

from page.base_page import BasePage
from up.test_lab.app.apppo.page.main_page import MainPage
import yaml

with open("../datas/caps.yml") as f:
    datas = yaml.safe_load(f)
    desires=datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']



class App(BasePage):
    def start(self):
        if self.driver == None:

            # 启动app
            caps = {}

            # 客户端与appium服务器建立连接的代码
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
            self.driver.launch_app()
        return self

    def restart(self):
        #重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self):
        # 完成页面的跳转，将self.driver传入MainPage页面
        return MainPage(self.driver)
