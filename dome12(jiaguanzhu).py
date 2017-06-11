#coding=utf-8
import unittest
from appium import webdriver
from time import sleep

class Weiboceshi(unittest.TestCase):
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)

    def xunzhao(self, by, locator):
        try:
            if by == 'id':
                self.driver.find_element_by_id(locator)
                return True
            elif by == 'name':
                self.driver.find_element_by_name(locator)
                return True
            elif by == 'content':
                self.driver.find_element_by_accessibility_id(locator)
        except:
            return False

    def test_addto(self):#加关注
        sleep(15)
        zho=self.xunzhao('content','我的资料')
        while zho is False:
            self.driver.press_keycode(4)
            zho=self.xunzhao('content','我的资料')
        self.driver.find_element_by_name('我的资料').click()
        self.driver.find_element_by_id('cabFollow').click()
        sleep(3)
        self.driver.find_element_by_xpath(xpath="//android.widget.TextView[@text='加关注']").click()
        sleep(3)
        self.driver.find_element_by_name('取消').click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)