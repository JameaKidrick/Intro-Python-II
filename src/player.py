# Write a class to hold player information, e.g. what room they are in
# currently.
import random

class Player:
    def __init__(self, name, current_room, *items, hp = 50, attack = 10, defense = 10):
        self.name = name
        self.current_room = current_room
        self.items = None
        self.hp = hp
        self.attack = attack
        self.defense = defense
    def travel(self, direction):
    # SEE IF THE CURRENT ROOM HAS THAT DIRECTION/ATTRIBUTE
        # GET ATTRIBUTE FINDS ATTRIBUTE, IF IT'S NOT THERE next_room WILL EQUAL None
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
        # SETS THE CURRENT ROOM TO THE ROOM THAT WE WENT TO
            self.current_room = next_room
            print(self.current_room)
        else:
            print("\n-----------------------------------------------------------------------\nYou cannot move in that direction")
    def get(self, item):
        if item != 'None':
            item_names = [i.name for i in self.current_room.items]
            if item in item_names:
                id = item_names.index(item)
                self.on_take(self.current_room.items[id].name)
                self.items.append(self.current_room.items[id])
                self.current_room.items.pop(id)
            else:
                print(f'That item isn\'t here')
        else:
            print('ERROR')
    def on_take(self, item):
        print(f'\n**You have picked up the {item}**')
    def drop(self, item):
        if item != 'None':
            item_names = [i.name for i in self.items]
            if item in item_names:
                if self.current_room.items == None:
                    id = item_names.index(item)
                    self.on_drop(self.items[id].name)
                    self.current_room.items = [self.items[id]]
                    self.items.pop(id)
                else:
                    id = item_names.index(item)
                    self.on_drop(self.items[id].name)
                    self.current_room.items.append(self.items[id])
                    self.items.pop(id)
            else:
                print(f'That item isn\'t here')
        else:
            print('ERROR')
    def on_drop(self, item):
        print(f'\n**You have dropped the {item}**')
    def fight(self, action):
        print(f'Monster HP: {self.current_room.monster.hp}')
        print(f'{self.name}\'s HP: {self.hp}')
        if action == 'attack':
            chance = random.randrange(1, 11)
            print('ATTACK')
            if chance == 1:
                print('...AND MISS')
            elif chance != 1:
                print('HIT')
                self.current_room.monster.hp = self.current_room.monster.hp - self.attack 
                print(f'Monster HP: {self.current_room.monster.hp}')
                print(f'{self.name}\'s HP: {self.hp}')
        else:
            print('DEFENSE')
        
    def run(self, cmd):
        directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
        print('\nYou ran!')
        self.travel(directions[cmd])
    def use(self):
        pass