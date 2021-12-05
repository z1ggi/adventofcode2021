boards = []
lastWinner = None
lastWinnerCall = None
loser = None
call = None

def readBoard(file, board):
  board = []
  for y in range(5):
    board.append(file.readline().strip('\n').split( ))
  boards.append(board)

def markBoards(boards, call):
  for board in boards:
    for line in board:
      try:
        line[line.index(call)] = 'x'
        break
      except:
        continue

def checkWinner(boards):
  for board in enumerate(boards):
    found = False
    for line in board[1]:
      if line.count('x') == 5:
        return board[0]
    for x in range(5):
      i = 0
      for y in range(5):
        if board[1][y][x] == 'x':
          i += 1
      if i == 5:
        return board[0]

def calculate(board, call):
  res = 0
  for line in board:
    for pos in line:
      try:
        res += int(pos)
      except:
        continue
  return res * int(call)


with open('./day4.txt', 'r') as file:
  calls = file.readline().strip('\n').split(',')
  while file.readline():
    readBoard(file, boards)
  
  while len(boards) and len(calls):
    call = calls.pop(0)
    markBoards(boards, call)
    while True:
      winner = checkWinner(boards)
      if winner is not None:
        lastWinner = boards.pop(winner)
        lastWinnerCall = call
      else:
        break
  print(calculate(lastWinner, lastWinnerCall))
