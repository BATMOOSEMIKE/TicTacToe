#This is the dictionary representing the game state, arranged as follows:
# 1 2 3
# 4 5 6
# 7 8 9
gameBoard = {
  1: '-', 2: '-', 3: '-',
  4: '-', 5: '-', 6: '-',
  7: '-', 8: '-', 9: '-'
}

#This helper function prints the game board
def printBoard(board):
  print(board[1] + " " + board[2] + " " + board[3])
  print(board[4] + " " + board[5] + " " + board[6])
  print(board[7] + " " + board[8] + " " + board[9])

#This helper function returns if there's a winner and prints corresponding output if there is
def checkWinner(board):
  if(board[1] == board[2] == board[3] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[1] + " has won the game")
    return True
  elif(board[1] == board[4] == board[7] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[1] + " has won the game")
    return True
  elif(board[1] == board[5] == board[9] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[1] + " has won the game")
    return True
  elif(board[2] == board[5] == board[8] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[2] + " has won the game")
    return True
  elif(board[3] == board[6] == board[9] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[3] + " has won the game")
    return True
  elif(board[4] == board[5] == board[6] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[4] + " has won the game")
    return True
  elif(board[7] == board[8] == board[9] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[7] + " has won the game")
    return True
  elif(board[7] == board[5] == board[3] != '-'):
    print()
    printBoard(gameBoard)
    print()
    print("The game is over!")
    print(board[7] + " has won the game")
    return True
  else:
    return False

#Main game function
def play():
  turn_count = 0
  cur_player = 'X'

  while(turn_count < 9):
    print("We are on turn number: " + str(turn_count+1))
    print("Here is the current state of the game: ")
    printBoard(gameBoard)
    print()
    print(cur_player + ", it is your turn. Choose a spot:")
    move = input()

    while(not move.isdigit() or int(move) > 9 or int(move) < 0 or (not gameBoard[int(move)] == '-')):
      move = input("Invalid move. Please enter a vacant spot (number) between 1 to 9: ")
    move = int(move)
    gameBoard[move] = cur_player
    if(checkWinner(gameBoard)):
      break
    if(cur_player == 'X'):
      cur_player = 'O'
    else:
      cur_player = 'X'
    print()
    turn_count += 1

  #Handling ties
  if(not checkWinner(gameBoard)):
    print()
    printBoard(gameBoard)
    print()
    print("The game is tied!")

if __name__ == "__main__":
  play()



