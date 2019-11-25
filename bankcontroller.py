from person import Person
from project1.card import Card


class BankController:
    def __init__(self):
        self.person_list = []
    # 重复确认密码
    def repeat_confirm(self,passwd,repasswd):
        # 确认密码是否正确
        if passwd == repasswd:
            return True
        return False
    # 开户(open)
    def open(self,person_tuple,money):
        if len(self.person_list):
            cardno = self.person_list[-1].card.cardno + 1
            card = Card(cardno,person_tuple[-1],money)
        else:
            card = Card(1000,person_tuple[-1],money)
        person = Person(person_tuple[0],person_tuple[1],person_tuple[2],card)
        self.person_list.append(person)
        return card
    # 存款(deposit)
    def deposit(self):
        pass
    # 查询(search)
    def search(self,cardno):
        for person in self.person_list:
            if person.card.cardno == cardno:
                return person.card
        return None
    # 取款(withdraw)
    def withdraw(self):
        pass
    # 转账(transfer)
    def transfer(self):
        pass
    # 销户(cancel)
    def cancel(self):
        pass
    # 锁定(locking)
    def lock(self):
        pass
    # 解锁(unlock)
    def unlock(self):
        pass
    # 补卡(card)
    def addcard(self):
        pass
    # 改密(passwd)
    def passwd(self):
        pass
    # 退出(quit)
    def quit(self):
        pass


