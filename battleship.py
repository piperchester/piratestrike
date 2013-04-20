# Original Developer: Kate Lockwood
#
# Piper Chester

import random

board = []
for x in range(0,5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return random.randint(0, len(board) -1)

def random_col(board):
    return random.randint(0, len(board[0]) -1)

def play_prompt(round_number):
  if round_number == 0:
    playing = raw_input("Ahoy there! Care for a game of battleship? ")
  else:
    playing = raw_input("Argh, how about another game? ")
  if playing.upper() == "YES" or playing.upper() == "Y":
    if round_number == 0:
      print("\nShiver me timbers! All aboard the high seas!\n")
    else:
      print("Yahoo! Time for round " + str(round_number + 1) + "!\n") 
    play_game(round_number) 
  else:
    print("Only " + str(round_number) + " rounds? I knew ye didn't have the stones...")

def play_game(round_number):
  round_count = round_number + 1
  print_board(board)

  ship_row = random_row(board)
  ship_col = random_col(board)

  guess_row = input("\nGuess Row: ")
  guess_col = input("Guess Col: ")

  if guess_row == ship_row and guess_col == ship_col:
      print("Curses! You sank my battleship!")
  else:
      if (guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4):
          print("\nAdjust your cannons swab, that's not even in the ocean.")
      elif board[guess_row][guess_col] == x:
          print("\nYou guessed that one already.")
      else:
          print("\nMUAHA! You missed my battleship!")
          print("She was lurking at " + str(ship_row) + ", " + str(ship_col)) 
          print("You guessed: " + str(guess_row) + ", " +  str(guess_col))
          play_prompt(round_count)

play_prompt(0)
