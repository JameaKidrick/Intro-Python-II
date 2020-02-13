# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def travel(self, direction):
      # SEE IF THE CURRENT ROOM HAS THAT DIRECTION/ATTRIBUTE
        # GET ATTRIBUTE FINDS ATTRIBUTE, IF IT'S NOT THERE next_room WILL EQUAL None
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
          # SETS THE CURRENT ROOM TO THE ROOM THAT WE WENT TO
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")