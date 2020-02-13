from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Boss', room['outside'])
currentRoom = Room(room[newPlayer.current_room].name, room[newPlayer.current_room].description, room[newPlayer.current_room].n_to, room[newPlayer.current_room].s_to, room[newPlayer.current_room].e_to, room[newPlayer.current_room].w_to)
# Write a loop that:
while True:

# * Prints the current room name
    print('Current Room:', newPlayer.current_room)
# * Prints the current description (the textwrap module might be useful here).
    # print(room[newPlayer.current_room].description, room[newPlayer.current_room].n_to.name, room[newPlayer.current_room].s_to.name, [newPlayer.current_room].e_to.name, room[newPlayer.current_room].w_to.name)

# * Waits for user input and decides what to do.
    cmd = input('Where would you like to go? Input `n` for North, `s` for South, `e` for East or `w` for West. If you would like to quit the game, press `q`. --> ')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if cmd == 'n':
        if room[newPlayer.current_room].n_to:
            newPlayer.current_room = room[newPlayer.current_room].n_to
            print('You moved north to', newPlayer.current_room)
        else:
            
            print('ERROR: You can\'t move in that direction. Try going s, e, w, or press q to quit.')
    elif cmd == 's':
        if room[newPlayer.current_room].s_to == None:
            print('ERROR: You can\'t move in that direction. Try going n, e, w, or press q to quit.')
        else:
            newPlayer.current_room = room[newPlayer.current_room].s_to
            print('You moved south to', newPlayer.current_room)
    elif cmd == 'e':
        if room[newPlayer.current_room].e_to == None:
            print('ERROR: You can\'t move in that direction. Try going n, s, w, or press q to quit.')
        else:
            newPlayer.current_room = room[newPlayer.current_room].e_to
            print('You moved east to', newPlayer.current_room)
    elif cmd == 'w':
        if room[newPlayer.current_room].w_to == None:
            print('ERROR: You can\'t move in that direction. Try going n, s, e, or press q to quit.')
        else:
            newPlayer.current_room = room[newPlayer.current_room].w_to.name
            print('You moved west to', newPlayer.current_room)
# If the user enters "q", quit the game.
    elif cmd == 'q':
        print('Thanks for playing! Goodbye!')
        exit()
    else:
        print('end')