from numpy import random

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
    print("{name} is now on square {pos}!".format(name = self.name, pos = self.position))
    return
      
class Board:
  def __init__(self):
    self.squares_remaining = 100
    self.snake_num = 8
    self.ladder_num = 8
    self.ladder_start_loc = []
    self.ladder_end_loc = []
    self.snake_start_loc = []
    self.snake_end_loc = []

  def __repr__(self):
    return print("This is the board of {squares} squares and has snakes located at {snake} and ladders located at {ladders}".format(squares = self.squares_remaining, snake = self.snake_loc, ladders = self.ladder_loc))

  def generate_snakes(self):
    for count in range(self.snake_num):
      self.snake_start_loc.append(random.randint(5, 99))
    print(self.snake_start_loc)
    for num in self.snake_start_loc:
      y = random.randint(5, 50)
      x = num - y
      if x <= 0:
        x = 5
      self.snake_end_loc.append(x)
    print(self.snake_end_loc)

  def generate_ladders(self):
    for count in range(self.ladder_num):
      self.ladder_start_loc.append(random.randint(5, 80))
    print(self.ladder_start_loc)
    for num in self.ladder_start_loc:
      y = random.randint(5, 30)
      x = num + y
      if x >= 90:
        x = 90
      self.ladder_end_loc.append(x)
    print(self.ladder_end_loc)
  
    
board = Board()
player = Player("Zo")

player.roll_dice()
player.advance()