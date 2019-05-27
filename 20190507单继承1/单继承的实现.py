from student import Student
from worker import Worker

xiaohong = Student("北京八环小富婆",  18, 127.5, 2012010540)
print(xiaohong.name, "高寿：" , xiaohong.age, xiaohong.stuId)
print(xiaohong.getMoney())
xiaohong.run()
xiaohong.eat("菠萝香蕉火龙果，馒头米饭和香锅。")

xiaoming = Worker("小明", 18, 100)
xiaoming.eat("土豆")