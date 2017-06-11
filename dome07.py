#coding=utf-8
import unittest
from appium import webdriver
from time import sleep



class Weiboceshi(unittest.TestCase):
    def setUp(self):                                                #点评
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)

    def test_Comment(self):
        sleep(20)
        self.driver.find_element_by_id('plus_icon').click()
        self.driver.find_element_by_name('点评').click()
        sleep(3)
        self.driver.find_element_by_name('神奇女侠').click()#不能使用xpath定位
        self.driver.find_element_by_name('写点评').click()
        dj=self.driver.find_elements_by_xpath(xpath="//android.widget.ImageView")
        dj[4].click()
        self.driver.find_element_by_id('edit_view').send_keys('luguo')
        self.driver.find_element_by_name('发送').click()





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)
