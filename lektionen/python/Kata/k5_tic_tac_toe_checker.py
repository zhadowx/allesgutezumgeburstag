def is_solved(board):
  #Check helper function
  def check(arr):
    for row in arr:
      if row.count(1) == 3:
        return 1
      if row.count(2) == 3:
        return 2
  #Column array
  columns = [[], [], []]
  for i in range(3):
    for j in range(3):
      columns[i].append(board[j][i])
  #Diagonal array
  diagonals = [[], []]
  for i in range(3):
    diagonals[0].append(board[i][i])  
    diagonals[1].append(board[i][2-i])
  #Results
  if check(board) != None:
    return check(board)
  elif check(columns) != None:
    return check(columns)
  elif check(diagonals) != None:
    return check(diagonals)
  else:
    for row in board:
      if 0 in row:
        return -1
    return 0



print(is_solved([[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]))