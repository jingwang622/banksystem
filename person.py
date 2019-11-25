from project1.card import Card


class Person:
    def __init__(self, name="", identification="", phone="",card = Card()):
        self.name = name
        self.identification = identification
        self.phone = phone
        self.is_administrator = False
        self.card = card

