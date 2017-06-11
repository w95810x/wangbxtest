#coding=utf-8
import unittest
from appium import webdriver
from time import sleep
                                                            #为什么微博前边不加test可以运行而微信不能
class Weixin(unittest.TestCase):


     def setup(self):
        jr={}
        jr['platformName']='Android'
        jr['platformVersion']='4.4.4'
        jr['deviceName']='5a20c8c'
        jr['appPackage']='com.tencent.mm'
        jr['appActivity']='com.tencent.mm.ui.LauncherUI'
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',jr)


     def test_dl(self):
         sleep(15)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Weixin)
    unittest.TextTestRunner(verbosity=2).run(suite)