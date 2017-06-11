#coding=utf-8
import unittest
from appium import webdriver
from time import sleep
class ContactsAndroidTests(unittest.TestCase):

    def setUp(self):
        getinto={}
        getinto['platformName']='Android'
            #平台名字=安卓
        getinto['platformVersion']='4.4.4'
            #平台版本=4.4.4
        getinto['deviceName']='5a20c8c'
            #设备名称=5a20c8c
        getinto['appPackage']='com.sina.weibo'
            #安装包=xxx
        getinto['appActivity']='com.sina.weibo.SplashActivity'
            #app活动=微博入口文件名
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',getinto)
            #这个对象的驱动方法=测试用例远程操作
    def test_zz(self):
        # self.signin()
        # self.fas()
        self.tuichu()

    def signin(self):
        sleep(20)
        self.driver.find_element_by_name('登录').click()
        self.driver.find_element_by_id('etLoginUsername').send_keys('15097475275')
        sleep(3)
        self.driver.find_element_by_id('etPwd').send_keys('9581083065')
        sleep(3)
        self.driver.find_element_by_name('登录').click()
        sleep(15)
        Verification=self.driver.find_element_by_name('春风冷8').text
        self.assertEqual(u'春风冷8', Verification)

    def fas(self):
        sleep(5)
        self.driver.find_element_by_id('plus_icon').click()
        self.driver.find_element_by_id('composer_item_image').click()
        self.driver.find_element_by_name('分享新鲜事...').send_keys('aaabbbccc')
        self.driver.find_element_by_id('titleSave').click()
        el = self.driver.find_elements_by_xpath(xpath="//android.widget.TextView")
        self.assertIn(u"aaabbbccc", el[4].text)

    def lookup(self,by,locator):
        try:# [traɪ]尝试
            if by == 'id':
                self.driver.find_element_by_id(locator)
                return True
            elif by == 'name':
                self.driver.find_element_by_name(locator)
                return True
            elif by == 'content':
                self.driver.find_element_by_accessibility_id(locator)
                return True
        except:# [ɪkˈsept] 除了
            return False

    def tuichu(self):
        my_button = self.lookup("content", "我的资料")

        while my_button is False:
            self.driver.press_keycode(4)
            my_button = self.lookup("content", "我的资料")
        self.driver.find_element_by_name('我的资料').click()
        self.driver.find_element_by_name('设置').click()
        self.driver.find_element_by_name('帐号管理').click()
        self.driver.find_element_by_name('退出当前帐号').click()
        self.driver.find_element_by_name('确定').click()


    def tearDown(self):
        self.driver.quit()





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)








