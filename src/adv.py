from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure  chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Set item placement
room['foyer'].items = [Item('Spear', 'A weak weapon. It looks well used. +10 damage'), Item('Note', 'It reads: \n\n     "I didn\'t make it far. The beast ahead is too strong. \n     If you are reading this, I\'ve given up the search to find the ring. \n     Good luck adventurer. \n\n     P.S. The sword is the only thing that can tame the beast."')]

room['overlook'].items = [Item('Bread', 'Gain +2 HP'), Item('Map', 'This shows the way out.')]

room['narrow'].items = [Item('Sword', 'Very sharp. +50 damage'), Item('Shield', 'Increase block by 25'), Item('Key', 'Unlocks something.')]

room['treasure'].items = [Item('Gold', '5,000 Gold!'), Item('Armor', 'Reduce damage taken by 25'), Item('Ring', 'My Precious!')]

#
# Main
#
name = input('What is your character\'s name? ')
# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(f'{name}', room['outside'])
newPlayer.items = [Item('Shirt', 'Basic. I need armor.'), Item('Stick', 'Breaks after 1 use. +3 damage.'), Item('Water', 'Gain +1 HP')]
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print(f'\n-----------------------------------------------------------------------\nCurrent Room: {newPlayer.current_room.name}\n\n{newPlayer.current_room.description}\n\nWithin the {newPlayer.current_room.name}, you see the following items:\n\n{newPlayer.current_room.items}\n-----------------------------------------------------------------------\n')

# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

while True:
    cmd = input(f'Where would {newPlayer.name} like to go? Input `n` for North, `s` for South, `e` for East or `w` for West. If you would like to quit the game, press `q`. --> ')
    # CHECKS IF INPUT IS WITHIN THE ARRAY
    if cmd in ['n', 's', 'e', 'w']:
        # MOVES TO ROOM USING TRAVEL METHOD
        newPlayer.travel(cmd)
        if newPlayer.current_room.items is not None:
            print(f'\nWithin the {newPlayer.current_room.name}, you see the following items:\n'
            )
            for i in newPlayer.current_room.items:
                print(f' * {i.name} - {i.description}')
            print('\n-----------------------------------------------------------------------\n')
        else:
            print('The room is empty')
    elif cmd == 'i' or cmd == 'inventory':
        if newPlayer.items is not None:
            print(f'{newPlayer.name}\'s inventory: \n')
            for i in newPlayer.items:
                print(f'* {i.name} - {i.description}')
        else:
            print(f'{newPlayer.name} has nothing in their inventory\n')
    elif cmd == 'help':
        print()
    elif cmd == 'q':
        # ENDS LOOP
        print('Thanks for playing! Goodbye!')
        exit()
    else:
        split = cmd.split(' ')
        if split[0] == 'get' or split[0] == 'take':
            newPlayer.get(split[1])
            if newPlayer.current_room.items is not None:
                print(f'\nWithin the {newPlayer.current_room.name}, you see the following items:\n'
                )
                for i in newPlayer.current_room.items:
                    print(f' * {i.name} - {i.description}')
                print('\n-----------------------------------------------------------------------\n')
            else:
                print('The room is empty')
            if newPlayer.items is not None:
                print(f'{newPlayer.name}\'s inventory: \n')
                for i in newPlayer.items:
                    print(f' * {i.name} - {i.description}')
            else:
                print(f'{newPlayer.name} has nothing in their inventory')
        elif split[0] == 'drop' or split[0] == 'remove':
            newPlayer.drop(split[1])
            if newPlayer.current_room.items is not None:
                print(f'\nWithin the {newPlayer.current_room.name}, you see the following items:\n'
                )
                for i in newPlayer.current_room.items:
                    print(f' * {i.name} - {i.description}')
                print('\n-----------------------------------------------------------------------\n')
            else:
                print('The room is empty')
            if newPlayer.items is not None:
                print(f'{newPlayer.name}\'s inventory: ')
                for i in newPlayer.items:
                    print(f' * {i.name} - {i.description}')
            else:
                print(f'{newPlayer.name} has nothing in their inventory')
        else:
            print('\n-----------------------------------------------------------------------\nI did not understand that command. Please input `n`, `s`, `e`, or `w`.\n-----------------------------------------------------------------------\n')
