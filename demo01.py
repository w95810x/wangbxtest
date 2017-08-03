#coding=utf-8
import unittest
from appium import webdriver
from time import sleep

class ContactsAndroidTests(unittest.TestCase):
        def setUp(self):
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '4.4'
            desired_caps['deviceName'] = '5a20c8c'
            # desired_caps['app'] = PATH(
            #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
            # 汉字前面加u改变编码为un...
            desired_caps['appPackage'] = 'com.sina.weibo'
            desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        def tearDown(self):
            self.driver.quit()

        def test_login(self):
            sleep(30)
            #找到元素
            el = self.driver.find_element_by_name("登录")
            #调用元素对象的点击方法
            el.click()
            #进入登录界面后定位找到输入账号的元素
            username = self.driver.find_element_by_id('etLoginUsername')
            #调用元素的输入内容方法
            username.send_keys("15097475275")
            pwd = self.driver.find_element_by_id('etPwd')
            pwd.send_keys("9581083065")
            button = self.driver.find_element_by_name('rlLogin')
            button.click()
            sleep(15)

        def test_reg(self):
            pass


        def test_loginout(self):
            pass




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



# a=8
#
# b=0
# while  b<= 2:
#     c = raw_input("请输入数字:")
#     if c.isdigit():
#        c = int(c)
#     if c > a:
#         print "数字大了"
#     elif c < a:
#         print "数字小了"
#     else:
#         print "恭喜你答对了!"
#         break
#
#     b += 1
# else:
#     print "今天已玩过三次请明天再来玩"


# a=18
# b=0
# while b<=2:
#     c=input("请输入数字：")
#     if c<a:
#         print "小了"
#     elif c>18:
#         print "大了"
#     elif c==a:
#         print "答对了"
#         break
#     b+=1
# else:
#     print "三次够了，再见"


# sum=""
# while sum != "q":
#     print "heool"
#     sum=raw_input("请继续输入,q for quit:")
#     if not sum:
#         break

# class Studunt(object):
#     pass
# bart = Studunt()

# class student(object):
#     def __init__(self,yuwen,shuxue,yingyu):
#         self.yuwen = yuwen
#         self.shuxue = shuxue
#         self.yingyu = yingyu
#
#     def add(self):
#         return self.yuwen+self.shuxue+self.yingyu
#
#     def avg(self):
#         return self.add()/3
#
# s = student(98,77,56)
# zongfeng = s.add();
# print(zongfeng)
# pingjunfen = s.avg()
# print(pingjunfen)

#setup(self)每一个用例运行前都会执行
#tearDown没一个case运行完后用来清理环境

