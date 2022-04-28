from random import randint

board = []
boardgrid = input("Choose your desired length and width, from 3 to 9")
for x in range(int(boardgrid)):
  board.append(["O"] * int(boardgrid))

def print_board(board):
  for row in board:
    print((" ").join(row))

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

# This is the function that establishes the location of the hidden ship

# This class contains the necessary methods and variables for BATTLESHIP
        
class Ship(object):
        def __init__(self, length, width):
          self.length = length
          self.width = width
        # This is the function that establishes the location of the hidden ship
        def random_row(self, board):
          return randint((self.width -1), len(board) - (self.width))
        def random_col(self, board):
          return randint((self.length -1), len(board[0]) - (self.length))
        # This is the game method
        def game(self):
          x = self.width - 1
          y = self.length - 1
          ship_row = int(self.random_row(board))
          ship_col = int(self.random_col(board))
          ship_row2 = [] 
          ship_col2 = []
          while x >= 0:
            ship_row2.append(ship_row - x)
            ship_row2.sort()
            x = x - 1
          while y >= 0:
            ship_col2.append(ship_col - y)
            ship_row2.sort()
            y = y - 1 
          for turn in range(5):
            print("Turn {}".format(turn + 1))
            print_board(board)
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
            guess_full = [guess_row, guess_col]
            if guess_row in ship_row2 and guess_col in ship_col2:
              print("Congratulations! You sunk my battleship!")
              break 
            else:
              if (guess_row < 0 or guess_row > len(board) - 1) or (guess_col < 0 or guess_col > len(board) - 1):
                print("Oops, that's not even in the ocean.") 
              elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already.") 
              else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = "X"
  # Print (turn + 1) here!
            if turn == 4:
              print ("Game Over")
              break
        def debug(self):
          x = self.width - 1
          y = self.length - 1
          ship_row = int(self.random_row(board))
          ship_col = int(self.random_col(board))
          ship_row2 = [] 
          ship_col2 = []
          a = ship_row
          b = ship_col
          while x >= 0:
            ship_row2.append(ship_row - x)
            ship_row2.sort()
            x = x - 1
          while y >= 0:
            ship_col2.append(ship_col - y)
            ship_row2.sort()
            y = y - 1 
          # Gameplay loop starts here
          for turn in range(5):
            print("Turn {}".format(turn + 1))
            while a > (ship_row - self.width):
              while b > (ship_col - self.length):
                board[a][b] = "Y"
                b = b - 1
              b = ship_col
              a = a - 1
            print_board(board)
            print (ship_row2)
            print (ship_col2)
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
            if guess_row in ship_row2 and guess_col in ship_col2:
              print("Congratulations! You sunk my battleship!")
              break 
            else:
              if (guess_row < 0 or guess_row > len(board) - 1) or (guess_col < 0 or guess_col > len(board) - 1):
                print("Oops, that's not even in the ocean.") 
              elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already.") 
              else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = "X"
  # Print (turn + 1) here!
            if turn == 4:
              print ("Game Over")
              break    
easy_mode = Ship(2, 2)
medium_mode = Ship(1, 2)
hard_mode = Ship(1, 1)
debog_mode = Ship(3, 3)
# Here the user is prompted to select a difficulty

def select_screen():
  print(""" 
                                          B A T T L E S H I P                                                                   

   




                                          SELECT A DIFFICULTY
                                              
                                                1 - EASY
                                                2 - NORMAL
                                                3 - HARD


""")
  difficulty = str(input())
  if difficulty == '1':
    easy_mode.game()
  elif difficulty == '2':
    medium_mode.game()
  elif difficulty == '3':
    hard_mode.game()
  elif difficulty == '4D':
    debog_mode.debug()

select_screen()

def battleship_launch():
  select_screen()
