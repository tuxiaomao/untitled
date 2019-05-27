
class Person(object):
    # 这里的属性是类属性（用类名来调用）类似于Java的静态属性
    name = "hanmeimei"
    def __init__(self, name):
        # 对象属性
        self.name = name

# 对象属性的优先级高于类属性
print(Person.name)

per = Person("tom")
print(per.name)

# 可以给对象动态添加对象属性,只对当前对象有效
per.age = 18

# 删除对象的name属性，会使用同名的类属性
del per.name
print(per.name) #此处会打印类属性“hanmeimei”

# 注意：以后千万不要将对象属性与类属性同名，因为对象属性会屏蔽类属性。但是删除对象属性后，就能使用类属性了。


