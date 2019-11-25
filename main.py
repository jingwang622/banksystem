# -*- coding：utf-8 -*-
from project1.bankview import BankView


def main():
    view = BankView()
    view.show_surface()
    while True:
        business = input("请输入您的操作:")
        choose_business(business,view)


def choose_business(business,view):
    # 开户
    if business == "open":
        view.open_account()
    # 存款
    elif business == "deposit":
        pass
    # 查询
    elif business == "search":
        view.search_account()
    # 取款
    elif business == "withdraw":
        pass
    # 转账
    elif business == "transfer":
        pass
    # 销户
    elif business == "cancel":
        pass
    # 锁定
    elif business == "locking":
        pass
    # 解锁
    elif business == "unlock":
        pass
    # 补卡
    elif business == "card":
        pass
    # 改密
    elif business == "passwd":
        pass
    else:
        pass


if __name__ == '__main__':
    main()