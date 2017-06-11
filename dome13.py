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

    def xunzhao(self,by,locator):
        try:
            if by=='id':
                self.driver.find_element_by_id(locator)
                return True
            elif by=='name':
                self.driver.find_element_by_name(locator)
                sleep(10)
                return True
            elif by=='content':
                self.driver.find_element_by_accessibility_id(locator)
                return True
        except:
            return False



    def test_zhaoyinyue(self):
        sleep(15)
        self.driver.find_element_by_id('plus_icon').click()
        self.driver.swipe(479,400,1,400)
        self.driver.find_element_by_name('音乐').click()
        sleep(5)
        zhao=self.xunzhao('name','我-张靓颖')
        while zhao is False:
            self.driver.swipe(100,750,100,200,2000)
            zhao = self.xunzhao('name', '我-张靓颖')
        self.driver.find_element_by_class_name('android.widget.LinearLayout').click()
        self.driver.find_element_by_name('发送')













if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)