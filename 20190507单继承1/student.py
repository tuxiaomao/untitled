from person import Person

class Student(Person):
    def __init__(self, name, age, money, stuId):
        #调用父类的__init__,这是最标准的写法
        super(Student,self).__init__(name, age, money)
        #子类可以有自己独有的属性
        self.stuId = stuId





