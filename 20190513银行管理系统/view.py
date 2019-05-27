from time import time

class View(object):

    admin = "1"
    pwd = "1"

    def printAdminView(self):
        print("***********************************************************")
        print("*                                                                            *")
        print("*                                                                            *")
        print("*                     欢迎登录非正规银行                         *")
        print("*                                                                            *")
        print("*                                                                            *")
        print("***********************************************************")
        inputAdmin = input("请输入管理员账号：")
        if inputAdmin != self.admin:
            print("账号输入有误！")
            return -1
        inputPwd = input("请输入管理员密码：")
        if inputPwd != self.pwd:
            print("密码输入错误！")
            return -1

        #能执行到这里说明账号密码正确
        print("登录成功！请稍候……")
        time.sleep(2)

        return 0



    def printSysFunctionView(self):
        print("***********************************************************")
        print("*     开户(1)                                   查询(2)              *")
        print("*     取款(3)                                   存款(4)              *")
        print("*     转账(5)                                   改密(6)              *")
        print("*     锁定(7)                                   解锁(8)              *")
        print("*     补卡(9)                                   销户(0)              *")
        print("*                            退出(q)                                     *")
        print("***********************************************************")













