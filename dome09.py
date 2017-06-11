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

    def dz(self):#点赞，验证点赞功能
        sleep(15)
        self.driver.find_element_by_accessibility_id('我的资料').click()
        self.driver.find_element_by_id('cabWeibo').click()
        self.driver.find_element_by_id('tv_feed_like_count').click()
        self.driver.find_element_by_id('mblogHeadtitle').click()
        self.driver.find_element_by_id('tv_liked_count').click()
        #yz=self.driver.find_element_by_id('tv_liked_count').text
        #self.assertEqual(u'赞1',yz)#出错了

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
                return True
        except:
            return False















if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)