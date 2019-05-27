import time
import datetime
'''
#返回当前时间的时间戳，浮点数形式，不需要参数
presentTime = time.time()
print("当前时间戳为（距离1970年1月1日的秒数）：",presentTime)

#将时间戳转化为UTC时间元组
gmTime = time.gmtime(presentTime)
print("当前时间戳转UTC（格林尼治时间）为：",gmTime)

#将时间戳转为本地时间元组
localTime = time.localtime(presentTime)
print("当前时间戳转本地时间元组为：",localTime)

#将本地时间元组转为时间戳
standardTime = time.mktime(localTime)
print("本地时间元组转时间戳为：",standardTime)

#将时间元组转成字符串
timeStr = time.asctime(localTime)
print("本地时间元组转字符串为：",timeStr)

#将时间戳转为字符串（本地时间）
presentTimeStr = time.ctime(presentTime)
print("当前时间戳转字符串为：",presentTimeStr)

#将时间元组转换为给定格式的字符串，参数2为时间元组，如果没有参数2，默认转当前时间
myTimeStr = time.strftime("%Y-%m-%d %X",gmTime)
print("你自定义的时间元组转字符串为：",myTimeStr)
print(type(myTimeStr))

#将时间字符串转为时间元组
myTimeStr2Tuple = time.strptime(myTimeStr,"%Y-%m-%d %X")
print("你自定义的转字符串的时间元组为：",myTimeStr2Tuple)
print(type(myTimeStr2Tuple))

#延迟一个时间，整形或者浮点型
time.sleep(5)

#返回当前程序的CPU执行时间

#Unix系统始终返回全部的运行时间
#Windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数

cpuTime = time.process_time()
print(cpuTime)
time.sleep(1)
cpuTime1 = time.process_time()
print(cpuTime1)
time.sleep(1)
cpuTime2 = time.process_time()
print(cpuTime2)
'''

#获取当前时间
dTime = datetime.datetime.now()
print(dTime)