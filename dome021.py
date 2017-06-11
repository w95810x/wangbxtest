#coding=utf-8
m='nan'
f='nv'

age=float(raw_input("输入你的年龄:"))
xb=raw_input("输入你的性别： ")
if 10<= age<=12 and xb==f:
    print "通过"
elif age>=13 and xb==f:
    print '年龄太大了'
elif age<10 and xb==f:
    print '年龄太小了'
if 10<= age<=12 and xb==m:
    print "去男足报名"
elif age>=13 and xb==m:
    print '年龄太大了,去男足报名'
elif age<10 and xb==m:
    print '年龄太小了没，去下一级报名'
else:
    print '系统异常！'


