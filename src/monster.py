class Monster:
    def __init__(self, name, room, hp = None, attack = None, defense = None):
        self.name = name
        self.room = room
        self.hp = hp
        self.attack = attack
        self.defense = defense
    # add chance for attack (70%) and chance for defense (20%) and chance for miss (10%)
    # if hp below certain point increase chance for defence
    def attack(self):
        pass
    def defend(self):
        pass