""" Game classes """

class Room:
    """ Room class """
    def __init__(self, name) -> None:
        """ Initialize class inctance """
        self.name = name
        self.__item = None
        self.linked_rooms = {}
        self.character = None
        self.description = ""

    def set_item(self, item):
        """ Sets item to the room """
        self.__item = item
    def link_room(self, room, direction):
        """ Links one room to another through "direction" variable """
        self.linked_rooms[direction] = room
    def set_character(self, character):
        """ Sets character into the room """
        self.character = character
    def set_description(self, description):
        """ Sets description about the room """
        self.description = description
    def get_details(self):
        """ Prints into console details about the room """
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, place in self.linked_rooms.items():
            print(f"The {place.name} is {direction}")
    def get_character(self):
        """ Returns character in the room """
        return self.character
    def get_item(self):
        """ Returns item in the room """
        return self.__item
    def move(self, direction):
        """
        Returns room based on given direction.
        If there is no place in given direction than the same room will be returned
        """
        if direction not in self.linked_rooms:
            return self
        return self.linked_rooms[direction]

class Character:
    """ Character class """
    def __init__(self, name, description) -> None:
        """ Initialize class inctance """
        self.conversation = ""
        self.name = name
        self.description = description
        self.weakness = ""

    def set_weakness(self, weakness):
        """ Sets weakness to character """
        self.weakness = weakness
    def set_conversation(self, conversation):
        """ Sets converation script to character """
        self.conversation = conversation
    def describe(self):
        """ Prints into console description about character """
        print(f"{self.name} is here!")
        print(self.description)
    def talk(self):
        """ Prints into console talk of character """
        print(f"[{self.name} says]: {self.conversation}")


class Enemy(Character):
    """ Enemy class """
    defeated = 0
    def __init__(self, name, description) -> None:
        """ Initialize class inctance """
        super().__init__(name, description)

    def get_defeated(self):
        """ Returns quanetity of Enemies got defeated """
        return Enemy.defeated

    def fight(self, fight_with):
        """ Returns true if "fight_with" item is weakness of particular enemy """
        if self.weakness == fight_with:
            Enemy.defeated += 1
            return True
        return False

class Friend(Character):
    """ Friend class """
    def __init__(self, name, description) -> None:
        """ Initialize class inctance """
        super().__init__(name, description)

class Item:
    """ Item class """
    def __init__(self,name) -> None:
        """ Initialize class inctance """
        self.description = ""
        self.name = name

    def set_description(self, description):
        """ Sets description to Item object """
        self.description = description
    def describe(self):
        """ Prints into console info about item """
        print(f"The [{self.get_name()}] is here - {self.description}")
    def get_name(self):
        """ Returns item name """
        return self.name
