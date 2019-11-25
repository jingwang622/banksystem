from project1.bankcontroller import BankController


class BankView:
    def __init__(self):
        self.bankcontroller = BankController()

    def show_surface(self):
        print(
      """
      开户(open)        存款(deposit)
      查询(search)      取款(withdraw)

      转账(transfer)    销户(cancel)
      锁定(locking)     解锁(unlock)

      补卡(card)        改密(passwd)

                退出(quit)

                王静私人银行 
      """
        )
    def open_account(self):
        person_tuple = self.input_person_info()
        num = 3
        # 请为银行卡确认密码：
        while num:
            num -= 1
            repasswd = input("请为银行卡确认密码：")
            if self.bankcontroller.repeat_confirm(person_tuple[3],repasswd):
                money = float(input("请输入您的预存款"))
                card = self.bankcontroller.open(person_tuple, money)
                print("开户成功！请牢记您的银行卡号：%d" % card.cardno)
                break
        else:
            print("确认密码输入有误")
    def search_account(self):
        # 请输入银行卡号：
        cardno = input("请输入银行卡号：")
        card_info = self.bankcontroller.search(cardno)
        if card_info:
            # 请输入银行卡密码：
            password = input("请为银行卡输入密码:")
            if self.bankcontroller.repeat_confirm(card_info.passwd,password):
                print("卡号%d   余额：%f"%(card_info.cardno,card_info.money))
            else:
                print("此卡被锁定，请解锁后办理其他业务！")
        else:
            print("没有此银行卡信息！")

    def input_person_info(self):
        # 请输入姓名：
        name = input("请输入姓名:")
        # 请输入身份证号：
        identification = input("请输入身份证号:")
        # 请输入电话号码：
        phone = input("请输入电话号码：")
        # 请为银行卡输入密码：(已输入123但不显示)
        password = input("请为银行卡输入密码:")
        return (name,identification,phone,password)


