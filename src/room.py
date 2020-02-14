# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, *items):
        self.name = name
        self.description = description
        # SETTING INITIAL DIRECTIONS TO None
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = None
    def __str__(self):
        return f'\n-----------------------------------------------------------------------\nCurrent Room: {self.name}\n\n{self.description}'