#coding=utf-8
import unittest
from time import sleep
from appium import webdriver


class Weiboceshi(unittest.TestCase):                #添加频闭关键词
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)

    def test_pinbi(self):
        sleep(15)
        self.driver.find_element_by_id('titleSave').click()
        self.driver.find_element_by_name('屏蔽设置').click()
        self.driver.find_element_by_name('关键词').click()
        sleep(3)
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('sb')
        sleep(5)
        self.driver.find_element_by_name('添加').click()
        self.driver.find_element_by_name('确定').click()
        self.driver.tap([(40,580)])
        self.driver.find_element_by_id('titleBack').click()
        self.driver.find_element_by_id('titleBack').click()






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)
