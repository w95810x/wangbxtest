#coding=utf-8
from appium import webdriver
from time import sleep
import unittest

#################################################验证微博版本
class Weiboceshi(unittest.TestCase):
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)

    def test_qingchuhuancun(self):
        sleep(15)
        self.driver.find_element_by_accessibility_id('我的资料').click()
        self.driver.find_element_by_name('设置').click()
        self.driver.find_element_by_name('清除缓存').click()
        self.driver.find_element_by_name('确定').click()
        ####################################################缓存已清除无法捕捉



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)
