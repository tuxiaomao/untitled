class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0


    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def say(self):
        print("My name is %s,I am %d years old" % (self.name,self.age))


    # 构造函数，创建对象时默认的初始化
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        print("哈喽！我是%s，我今年%d岁了。" %(self.name,self.age))

    # 析构函数，用于释放对象。一般很少写，程序结束时会自动释放对象
    def __del__(self):
        print("这里是析构函数。")


person = Person("小米",25,160,55)

person.eat("apple")

# 释放对象,可以不手动释放，程序结束会自动释放
del person
# 对象释放后就不能再访问了,下方一行代码会报错
# person.age

# 在函数里定义的对象，会在函数结束时自动释放。可以减少内存空间的浪费
def function():
    person1 = Person("小明",5,120,28)

function()