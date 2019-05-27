from types import MethodType

#创建一个空类
class Person(object):
    __slots__ = ("name", "age", "speak")

per = Person()
# 动态添加属性，这体现了动态语言的特点（灵活）
per.name = "tom"
print(per.name)
#动态方法
def say(self):
    print("my name is " + self.name)
'''
这种方法不对
per.speak = say
per.speak(per)
'''
# MethodType是一种偏函数，可以用来给对象动态添加方法
per.speak = MethodType(say, per) #这样，say方法就变成了对象实例per的对象方法

per.speak()

# 思考：如何限制实例的属性？
# eg.只允许给对象添加name、age、height、weight属性
# 解决：定义类的时候，定义一个特殊的变量__slots__,可以限制动态添加的属性
# per.height = 165
# print(per.height)#运行会报错




