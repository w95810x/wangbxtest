#coding=utf-8
# print "这iprogram cinverts华氏摄氏度"
# print "在华氏温度的tempemperature型:",
# fahrenheit = float(raw_input())
# celsius = (fahrenheit-32)*5.0/9
# print "这是",
# print celsius,
# print "摄氏度"

# print "这是华氏转摄氏温度"
# b=input("华氏温度为：")
# a=(b-32)*5/9
# print "这是",a,"摄氏度"
import webbrowser


class Kaiguan:

    def kg(self):

        if self.fx=="guan":
            self.fx="kai"

mykaiguan=Kaiguan()
mykaiguan.fx="guan"
print "现在的状态是",mykaiguan.fx
print '我要关闭他'
print
mykaiguan.kg()
print '现在的状态是',mykaiguan.fx