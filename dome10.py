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


    def test_shot(self):#拍摄     #取不到下标
        sleep(15)
        self.driver.find_element_by_id('plus_icon').click()

        self.driver.find_element_by_name('拍摄').click()
        sleep(10)
        self.driver.find_element_by_id('camera_switch').click()
        sleep(3)
        self.driver.find_element_by_id('camera_bottom_middle').click()
        a=self.driver.find_elements_by_xpath(xpath="//android.widget.ImageView")
        a[3].click()#取不到想要的下标
        self.driver.find_element_by_name('下一步').click()
        self.driver.find_element_by_id('edit_view').send_keys('kuaile')
        self.driver.find_element_by_name('发送').click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)