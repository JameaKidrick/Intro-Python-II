# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, *items):
        self.name = name
        self.current_room = current_room
        self.items = None
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