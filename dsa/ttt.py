import math
import sys
import math


class Board:

  def __init__(self, player = 'max'):
    self.board = [' ' for _ in range(9)]
    self.player = player
    self.flag = True

  def displayBoard(self):
    for i in range(3):
      print("|", end='')
      for j in range(3):
        print(f" {self.board[i * 3 + j]} |", end='')
      print('')


  def minmax(self, board, isMax = False):
    
    if self.checkBoardStatus() == 'X':
      return 1, 11
    elif self.checkBoardStatus() == 'O':
      return -1, 11
    elif ' ' not in board:
      return 0, 11

    bestScore = math.inf if not isMax else -math.inf

    for i in range(len(board)):
      if board[i] == ' ':
        board[i] = 'X' if isMax else 'O'
        score, _ = self.minmax(board, not isMax)
        board[i] = ' '
        if (isMax and score > bestScore) or (not isMax and score < bestScore):
          bestScore = score
          bestPos = i

    return bestScore, bestPos



  def checkBoardStatus(self):
    win_conditions = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Anti-diagonal
    ]
    
    for a, b, c in win_conditions:
        if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
            return self.board[a]  

    if ' ' not in self.board:
      return 'tie'

    return None
    

  def checkWinnerOrTie(func):
      def wrapper(self, mark, player):
          func(self, mark, player)

          self.displayBoard()
          boardOutput = self.checkBoardStatus()
          if boardOutput == 'X' or boardOutput == 'O' or boardOutput == 'tie':
            #   print(f"The Output is {boardOutput}")
            if boardOutput == 'X':
              print("HUMAN WINS !!!!!!!!!")
            elif boardOutput == 'O':
              print("AI WINS !!!!!!!!!")
            elif boardOutput == 'tie':
              print("IT'S A TIE !!!!!!!!")
            
            sys.exit()
          return

      return wrapper



  @checkWinnerOrTie
  def updateBoard(self, mark, player):
    if self.board[mark-1] != ' ' or mark-1 > 8 or mark-1 < 0:
      print("Invalid mark, please place it again ... ")
      self.flag = False
      return

    if player == 'max':
      self.flag = True
      self.board[mark-1] = 'X'
      self.player = 'min'
    elif player == 'min':
      self.flag = True
      self.board[mark-1] = 'O'
      self.player = 'max'

      




board = Board()
while True:
  # print(f"Hello player {board.player}, please input the mark", end = ' ')
  # mark = int(input())
  # if mark == 11:break
  # board.updateBoard(mark, board.player)


# HUMAN V/S AI   ---- Above code is for human v/s human

  print(f"Hello Human Player,  please input the mark 'X' :  ", end = '')
  mark = int(input())
  if mark == 11 : break
  board.updateBoard(mark, 'max')
#   print(f"Board is : {board.board},  the flag is {board.flag}")
  if board.flag is True:
    print("AI's TURN")
    _, aiMark = board.minmax(board.board)  
    board.updateBoard(aiMark+1, 'min')



