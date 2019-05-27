class Person(object):
    # 实现人喂食任何动物，传入动物类变量即可，所有继承它的(动物)类都能被喂食
    def feedAnimal(self, animal):
        print("人投放食物")
        animal.eat()
