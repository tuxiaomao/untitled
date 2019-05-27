from animal import Animal
class Mouse(Animal):
    def __init__(self, name):
        # 一般的初始化为下一行
        # self.name = name
        # 用继承实现初始化，这是标准写法，cat里是另一种写法
        super(Mouse, self).__init__(name)



    # def eat(self):
    #     print(self.name + "吃")