#coding=utf-8
import unittest
from appium import webdriver
from time import sleep


class Weiboceshi(unittest.TestCase):                #看NBN视频
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)


    def test_monidianji(self):
        sleep(20)
        self.driver.tap([(290,790)])
        sleep(3)
        self.driver.tap([(240,450)])
        sleep(5)
        self.driver.tap([(160,810)])
        sleep(5)
        self.driver.tap([(20,200)])
        sleep(10)
        self.driver.find_element_by_id('video_list_tool_bar_close_view').click()
        self.driver.find_element_by_id('titleBack').click()
        self.driver.find_element_by_id('titleBack').click()




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)
