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

    # def test_dsf(self):
    #     sleep(15)
    #     self.driver.find_element_by_name('登录').click()
    #     a=self.driver.find_elements_by_xpath(xpath="//android.widget.ImageView")
    #     a[2].click()
    #     sleep(10)
    def test_deleterweibo(self):
        sleep(15)
        self.driver.find_element_by_accessibility_id('我的资料').click()
        self.driver.tap([(5,300)])
        sleep(3)
        self.driver.find_element_by_id('mblogHeadtitle').click()
        self.driver.find_element_by_id('detail_activity_header_right_button_text').click()
        sleep(3)
        self.driver.find_element_by_name('删除').click()
        self.driver.find_element_by_name('确定').click()
        self.driver.find_element_by_accessibility_id('更多操作').click()
        self.driver.find_element_by_name('返回首页').click()


#删除微博


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)

