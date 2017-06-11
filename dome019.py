#coding=utf-8
import unittest
from appium import webdriver
from time import sleep
                                              #使用class不稳定
class Weiboceshi(unittest.TestCase):
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)


    def test_ys(self):
        sleep(15)
        self.driver.find_element_by_accessibility_id('我的资料').click()
        self.driver.find_element_by_id('titleSave').click()
        self.driver.find_element_by_name('隐私设置').click()
        sleep(10)
        self.driver.find_element_by_accessibility_id('允许给我推荐通讯录好友 Link').click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('允许通过此手机号搜到我 Link').click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('允许评论带图 Link').click()
        sleep(5)
        a=self.driver.tap([(420,80)])
        sleep(3)
        self.driver.find_element_by_name('返回首页').click()
        sleep(3)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)
