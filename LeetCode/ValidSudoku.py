# Valid Sudoku from LeetCode #

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

#The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


def box_values(board, row, column):
  """Returns all the integer values in a given box"""
  values = []
  for r in range(row, row+3):
    for c in range(column, column+3):
      if board[r][c].isnumeric():
        values.append(int(board[r][c]))
  return values
      
def isValidSudoku(board):
  # Validate boxes
  for i in range(0, len(board)-3, 3):
    for j in range(0, len(board)-3, 3):
      values = box_values(board, i, j)
      values_set = set(values)
      if len(values) != len(values_set):
        return False
  # Validate rows
  for row in board:
      row_values = [el for el in row if el.isnumeric()]
      row_set = set(row_values)
      if len(row_values) != len(row_set):
          return False
  # Validate columns
  for c in range(len(board)):
      column_values = []
      for r in range(len(board)):
          if board[r][c].isnumeric():
            column_values.append(board[r][c])
      column_set = set(column_values)
      if len(column_values) != len(column_set):
          return False
  return True


if __name__ == '__main__':
    true_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

    false_board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

    false_board2 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    ["7",".",".",".","8",".",".","7","9"]
    ]

    print(isValidSudoku(true_board), True)
    print(isValidSudoku(false_board), False) # box values are the same
    print(isValidSudoku(false_board2), False) # column values are the same

