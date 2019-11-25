class Card:
    def __init__(self, cardno = 0,passwd="", money=0.0):
        self.cardno = cardno
        self.passwd = passwd
        self.money = money
        self.islock = False
