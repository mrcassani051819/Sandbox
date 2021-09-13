print("Welcome to 'Escape the Jail'!")
start_sig = False

while not start_sig:
    print("Type 'start' to begin the adventure, or you can type 'quit' or 'exit' to leave.")
    action = input().strip()
    if "start" in action:
        break
    elif action in [ "quit", "exit" ]:
        quit()
    else:
        pass

# A Room class. Rooms are linked nodes in a 'tree-like' structure.
class Room:
    def __init__(self, name="", north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west

# A Narrator class. It acts as an 'observer' class for the Player class. The Player notifies the Narrator when it acts.
class Narrator:
    def __init__(self):
        self.room_descriptions = {
            "cell": "It's a pretty severe jail cell. There's a broken toilet and a sink in one corner. There's a window to the west. You find the door to your cell to your east.",
            "jail hall": "A hall inside the jail. It links your cell with two others. There's a door to the north leading further into the jail.",
            "main room": "You're in a large room. If you had to guess, you'd say it appears to be the police precinct's bullpen. You know, like you've seen on TV. You can see the front door to the north!",
            "outside": "It's outside. It's freedom."
        }
    
    def get_narration(self, category, name):
        if "rooms" in category:
            if name in self.room_descriptions.keys():
                print(self.room_descriptions[name])

    def intro(self):
        print("You awaken in a cold, dark cell. You don't know who captured you, or why.")
    
    def action_disallowed(self):
        print("You can't do that.")

    def direction_missing(self):
        print("You didn't say which direction to do that.")

    def not_a_direction(self, bad_direction):
        print(bad_direction + " is not a direction.")

    def path_blocked(self):
        print("You can't go that way right now.")

    def location_changed(self, origin, destination):
        if "cell" in origin and "jail hall" in destination:
            print("You open the door to your cell and move carefully into the hallway.")
        elif "jail hall" in origin and "cell" in destination:
            print("You duck back into your cell. You should probably get moving in case anyone comes looking for you.")
        elif "jail hall" in origin and "main room" in destination:
            print("The hallway deposits you into a large room. There are lots of disorganized-looking desk with heaps of paperwork on them. Everything looks dusty.")
        elif "main room" in origin and "jail hall" in destination:
            print("You head back down the hallway. You're not sure if someone might come for you, but you think twice about still being here if anyone does.")
        elif "main room" in origin and "outside" in destination:
            print("You open the door the police station and step out into a dewy night. It's oddly quiet for the city. A rush goes up your spine: You made it out. What now?")
    
    def sign_off(self):
        print("Goodbye! Thanks for playing!")

    def congratulate(self):
        print("You've escaped! Congratulations, you win!")

# A Player class. A Player can move and perform other actions like 'look', 'examine' and 'grab' using the command method, which may call helper methods.
# An instance of Player is 'observed' by a Narrator object.
class Player:
    def __init__(self, narrator=None, start=None):
        self.narrator = narrator
        self.location = start

    def command(self, action, target=None):
        if "look" in action:
            narrator.get_narration("rooms", self.location.name)
            pass
        elif "move" in action:
            if not target:
                narrator.direction_missing()
                pass
            elif "north" in target:
                self.move("north")
            elif "south" in target:
                self.move("south")
            elif "east" in target:
                self.move("east")
            elif "west" in target:
                self.move("west")
        elif "quit" in action or "exit" in action:
            narrator.sign_off()
            exit()
        else:
            narrator.action_disallowed()
            pass

    def move(self, direction):
        start_location = self.location
        if "north" in direction:
            destination = self.location.north
        elif "south" in direction:
            destination = self.location.south
        elif "east" in direction:
            destination = self.location.east
        elif "west" in direction:
            destination = self.location.west
        else:
            narrator.not_a_direction(direction)
            pass
        if not destination:
            narrator.path_blocked()
            pass
        else:
            self.location = destination
            narrator.location_changed(start_location.name, destination.name)

# Initialize the game's objects.
start = Room("cell")
jail_hall = Room("jail hall")
main_room = Room("main room")
outside = Room("outside")

jail_hall.west = start
start.east = jail_hall
jail_hall.north = main_room
main_room.south = jail_hall
main_room.north = outside
outside.south = main_room

narrator = Narrator()
player = Player(narrator, start)
narrator.intro()

# The game should only be operated by passing commands to the Player object. The Narrator object will then report on actions taken by the Player object
while "outside" not in player.location.name:
    print("What do you do?")
    command = input().strip().split(" ")
    if len(command) == 1:
        player.command(command)
    elif len(command) > 1:
        if len(command) > 2:
            command = command[:2]
        player.command(command[0], command[1])
    else:
        pass

narrator.congratulate()
narrator.sign_off()
exit()
