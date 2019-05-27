class Gun(object):

    def __init__(self,bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.count == 0:
            print("没有子弹了")
        else:
            self.bulletBox.count -= 1
            print("还剩%d发子弹" %(self.bulletBox.count))