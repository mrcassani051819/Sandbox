print("Welcome to Escape the Maze!")
start = False

while not start:
    print("Type 'start' to begin, or type 'quit' or 'exit' if you don't want to play!")
    cmd = input().strip()
    if "start" in cmd:
        break
    elif "quit" or "exit" in cmd:
        quit()
    else:
        pass

class Room:
    def __init__(self, name=""):
        self.name = name
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def set_direction(self, direction, value):
        if "north" in direction:
            self.north = value
        elif "south" in direction:
            self.south = value
        elif "east" in direction:
            self.east = value
        elif "west" in direction:
            self.west = value
        else:
            pass

    def get_direction(self, direction):
        if "north" in direction:
            val = self.north
        elif "south" in direction:
            val = self.south
        elif "east" in direction:
            val = self.east
        elif "west" in direction:
            val = self.west
        else:
            pass
        return val

class Player:
    def __init__(self):
        self.location = None
    
    def move(self, direction):
        if "north" in direction:
            if self.location.north != None:
                self.location = self.location.north
            else:
                pass
        elif "south" in direction:
            if self.location.south != None:
                self.location = self.location.south
            else:
                pass
        elif "east" in direction:
            if self.location.east != None:
                self.location = self.location.east
            else:
                pass
        elif "west" in direction:
            if self.location.west != None:
                self.location = self.location.west
            else:
                pass
        else:
            pass

def get_player_input():
    print("Which way do you go? [ 'north', 'south', 'east', 'west' ]")
    response = input().strip()
    if response not in [ "north", "south", "east", "west" ]:
        response = get_player_input()
    return response

start = Room("start")
end = Room("end")

start.east = end
end.west = start

player = Player()
player.location = start

while "end" not in player.location.name:
    cmd = get_player_input()
    player.move(cmd)
