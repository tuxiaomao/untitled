class Person(object):

    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def say(self):
        print("My name is %s,I am %d years old" % (self.name,self.age))


    # 构造函数，创建对象时默认的初始化
    def __init__(self,name,age,height,weight,money):
        self.name = name
        self.__age__ = age #在Python中，__XX__属于特殊变量，可以直接访问
        self.height = height
        self._weight = weight  # Python中，_XXX 变量，这样的实例变量外部是可以访问的，但是，按照约定，视为私有变量，不要直接访问。
        self.__money = money #想要内部属性不被直接外部访问, 属性前加__，就变成了私有属性private。实际上是_Person__money
        print("哈喽！我是%s，我今年%d岁了。目前存款%f" %(self.name,self.__age__,self.__money))

    # 私有属性需要定义get、set方法来访问和赋值
    def setMoney(self, money):
        if (money < 0):
            self.__money = 0
        else:
            self.__money = money

    def getMoney(self):
        return self.__money


person = Person("小明", 5, 120, 28,93.1)

# 属性和特殊属性可直接被访问
print("小明的身高：%d" %person.height)
person.__age__ = 10
print("年龄已经改成了%d" %person.__age__)

# 私有属性不可直接被访问或赋值,因为解释器把__money变成了_Person__money（可以用这个访问到私有属性的money，但是强烈建议不要）,以下2行会报错
# person.money = 10
# print(person.__money)

# 可以调用内部方法访问和赋值
print(person.getMoney())
person.setMoney(-10)
print(person.getMoney())


