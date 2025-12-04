import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = 0
        self.position = 1
  
    def __repr__(self):
        return print("This is {name} they are at square {pos}.".format(name = self.name, pos = self.position))

    def roll_dice(self):
        roll = input("{name}, it's your go! When you are ready to roll the die, type roll:\n".format(name = self.name))
        while roll.lower() != "roll":
            roll = input("Take your time {name}, we are all waiting...\n".format(name = self.name))
        if roll.lower() == "roll":
            self.dice = random.randint(1, 6)
        print(self.dice)
    
    def advance(self):
        self.position += self.dice
        print("{name} rolled a {dice}! They are now on square {pos}.".format(name = self.name, dice = self.dice, pos = self.position))

    def land_on_obstical(self, ob_start, ob_end):
        for num in len(ob_start):
            if ob_start > ob_end[num]:
                self.position = ob_end[num]
                print("Oh no! {name} slid down a snake! They are now on square {pos}".format(name = self.name, pos = self.position))
            elif ob_start < ob_end[num]:
                self.position = ob_end[num]
                print("{name} has climbed a ladder! They are now on square {pos}.".format(name = self.name, pos = self.position))
      
      
    
class Board:
    def __init__(self):
        self.squares = 100
        self.snake_num = 8
        self.ladder_num = 8
        self.ladder_start_loc = []
        self.ladder_end_loc = []
        self.snake_start_loc = []
        self.snake_end_loc = []

    def __repr__(self):
        return print("This is the board of {squares} squares and has snakes located at squares {snake} and ladders located at squares {ladders}".format(squares = self.squares_remaining, snake = self.snake_loc, ladders = self.ladder_loc))

    def generate_snakes(self):
        for count in range(self.snake_num):
            self.snake_start_loc.append(random.randint(5, 99))
        for num in self.snake_start_loc:
            y = random.randint(5, 50)
            x = num - y
            if x <= 0:
                x = 5
            self.snake_end_loc.append(x)

    def generate_ladders(self):
        for count in range(self.ladder_num):
            self.ladder_start_loc.append(random.randint(5, 80))
        for num in self.ladder_start_loc:
            y = random.randint(5, 30)
            x = num + y
            if x >= 90:
                x = 90
            self.ladder_end_loc.append(x)

    def win(self, player_name):
        replay = input("{name} has won! They have landed on square 100! \n" 
        "Would you like to play again? \n"
        "(Press Q to quit, press R to replay)".format(name = player_name))
        while replay.lower() != "r" or replay.lower() != "q":
            replay = input("That wasn't right... lets try again. \n"
            "Press Q to quit, press R to replay")
        if replay.lower() == "r":
            game_start()
        elif replay.lower() == "q":
            sys.exit()
  
def game_start():
    board = Board()
    board.generate_snakes()
    board.generate_ladders()

    player_one_name = input("Welcome to snakes and ladders! This is a two player game, so grab a friend. First player, enter your name:\n")
    player_two_name = input("Second player, enter your name:\n")

    player_one = Player(player_one_name)
    player_two = Player(player_two_name)

    while player_one.position != board.squares and player_two.position != board.squares:
        player_one.roll_dice
        player_one.advance
        if player_one.position == board.snake_start_loc or player_one.position == board.ladder_start_loc:
            player_one.land_on_obstical
        player_two.roll_dice
        player_two.advance
        if player_two.position == board.snake_start_loc or player_two.position == board.ladder_start_loc:
            player_two.land_on_obstical
    if player_one.position == board.squares:
        board.win(player_one.name)
    if player_two.position == board.squares:
        board.win(player_two.name)

game_start()