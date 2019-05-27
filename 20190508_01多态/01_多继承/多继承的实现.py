from child import Child

def main():
    xiaohua = Child(30000,100)
    xiaohua.play()#父类Father方法
    xiaohua.eat()#父类Mother方法
    xiaohua.fun()#多继承的几个父类有相同名称的方法，继承对象列表第一个父类的方法

if __name__ == "__main__":
    main()