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

def update_board(col, row):
  board[col][row] = 'X'
  print_board(board)

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
      print("Shiver me timbers! All aboard the high seas!\n")
    else:
      print("Yahoo! Time for round " + str(round_number + 1) + "!\n") 
    play_game(round_number) 
  else:
      if round_number > 0:
        print("Only " + str(round_number) + " rounds? I knew ye didn't have the stones...")
      else:
          print("Avast. Be gone with ye!")

def play_game(round_number):
  round_count = round_number + 1
  shots = 3;
  print_board(board)

  ship_row = random_row(board)
  ship_col = random_col(board)

  while shots > 0:
    print("\nYou have " + str(shots) + " shots to sink my ship!")
    guess_row = input("\nGuess Row: ")
    guess_col = input("Guess Col: ")

    if guess_row == ship_row and guess_col == ship_col:
        print("Curses! You sank my battleship!")
        shots = 0
    else:
        if (guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4):
            print("\nAdjust your cannons swab, that's not even in the ocean.")
            shots -= 1;
        elif board[guess_row][guess_col] == x:
            print("\nYou guessed that one already.")
        else:
            print("\nSplash! Miss!\n")
            shots -= 1;
            update_board(guess_col, guess_row)
  
  
  print("BAHA! You're out of shops!")
  print("My ship was lurking at " + str(ship_row) + ", " + str(ship_col)) 
    
  play_prompt(round_count)

play_prompt(0)
