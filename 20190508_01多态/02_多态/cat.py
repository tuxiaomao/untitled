from animal import Animal

class Cat(Animal):
    def __init__(self, name):
        # 一般的初始化为下一行
        # self.name = name
        # 用继承实现初始化,这是一种写法，mouse里是标准写法
        Animal.__init__(self, name)

    # def eat(self):
    #     print(self.name + "吃")