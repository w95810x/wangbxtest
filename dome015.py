#coding=utf-8
import unittest
from time import sleep
from appium import webdriver


class Weiboceshi(unittest.TestCase):                #取消修改密码
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)



    def test_xiugaimima(self):
        sleep(15)
        self.driver.find_element_by_id('titleSave').click()
        self.driver.find_element_by_name('帐号与安全').click()
        self.driver.find_element_by_accessibility_id('修改密码1 Link').click()
        sleep(3)
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('9581083065')
        # self.driver.find_element_by_class_name('确定 Link').click()
        self.driver.find_element_by_accessibility_id('取消 Link').click()
        # self.driver.find_element_by_accessibility_id('下一步 Link').click()
        # self.driver.find_element_by_accessibility_id('立即编辑短信 Link').click()
        # self.driver.find_element_by_name('输入内容').send_keys('SGMM')
        # self.driver.find_element_by_name('SIM2').click()
        #信号不好不做了








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weiboceshi)
    unittest.TextTestRunner(verbosity=2).run(suite)
