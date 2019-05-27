'''银行自动提款机系统
人
类名：Person
属性：姓名、身份证号、电话号、卡
行为：

卡
类名：Card
属性：卡号、密码、余额
行为：

银行
类名：Bank
属性：用户列表、提款机


提款机
类名：ATM
属性：
行为：开户、查询、存款、取款、转账、改密、锁定、解锁、补卡、销户、退出

界面
类名：View
属性：
行为：管理员界面、管理员登录、系统功能界面
'''
from view import View


def main():
    view = View()
    # 管理员开机
    view.printAdminView()





if __name__ =="__main__":
    main()