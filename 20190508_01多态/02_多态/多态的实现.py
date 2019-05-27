#多态就是一种事物的多种形态，就是多个类继承一个父类（基本用不上）
from cat import Cat
from mouse import Mouse
from person import Person

tom = Cat("tom")
jerry = Mouse("jerry")

tom.eat()
jerry.eat()

xiaogang = Person()

#人喂食任何一种动物
xiaogang.feedAnimal(tom)
xiaogang.feedAnimal(jerry)



