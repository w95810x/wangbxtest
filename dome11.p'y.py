#coding=utf-8
import unittest
from appium import webdriver
from time import sleep

class Weiboceshi(unittest.TestCase):
    def setUp(self):                                                #点赞后验证
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)


    def xunzhao(self,by,locator):
        try:
            if by=='id':
                self.driver.find_element_by_id(locator)
                return True
            elif by=='name':
                self.driver.find_element_by_name(locator)
                return True
            elif by=='content':
                self.driver.find_element_by_accessibility_id(locator)
        except:
            return False




    def test_qiandao(self):  # 签到
        sleep(10)

        qd=self.xunzhao('content', '打开发布面板')

        while qd is False:
            self.driver.press_keycode(4)
            qd = self.xunzhao('content', '打开发布面板')
        self.driver.find_element_by_id('打开发布面板').click()
        self.driver.find_element_by_name('签到').click()
        self.driver.find_element_by_name('霍营').click()
        self.driver.find_element_by_id("edit_view").send_keys('abc')
        self.driver.find_element_by_name('发送').click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)