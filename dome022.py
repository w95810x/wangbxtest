#coding=utf-8
from appium import webdriver
from time import sleep
import unittest


class Weiboceshi(unittest.TestCase):
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)


    def test_kuaisutuodong(self):
        sleep(15)
        self.driver.find_element_by_accessibility_id('我的资料').click()
        self.driver.find_element_by_name('设置').click()
        self.driver.find_element_by_name('通用设置').click()

        a=self.driver.find_elements_by_class_name('android.widget.CheckBox')
        a[1].click()
        self.driver.find_element_by_id('titleBack').click()
        self.driver.find_element_by_id('titleBack').click()
        self.driver.find_element_by_accessibility_id('微博').click()
        self.driver.swipe(100,700,100,400)
        sleep(1)
       # self.driver.flick(478,184,478,785)                 没有实现





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)

