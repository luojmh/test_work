# coding:utf-8
# @Time:2021/2/27

import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
复用浏览器：关闭chrome，执行命令 chrome --remote-debugging-port=9222
使用cookies登陆时，取消复用浏览器
'''
class TestTmp():
    def setup_method(self, method):
        #复用浏览器
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)  # 复用浏览器()中添加 options=chrome_arg

    def teardown_method(self, method):
        self.driver.quit()



    def test_cookie_get(self):
        """
        基于浏览器复用,获取cookies并存入文件
        :return:
        """
        self.driver.get("https://www.baidu.com")
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies=self.driver.get_cookies()
        with open("tmp.text","w",encoding="utf-8") as f:
            json.dump(cookies,f)


    def test_cookie_login(self):
        """
        读取文件中的cookies，利用 cookies 进行登陆
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp.text", "r", encoding="utf-8") as f:
            cookies=json.load(f)

        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)


