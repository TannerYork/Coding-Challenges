def pascal_triangle(numRows):
  triangle = [[0] * i for i in range(1, numRows+1)]
  for i in range(numRows):
    if i > 0:
      row = triangle[i]
      prev_row = triangle[i-1]
      for j in range(len(row)):
        x = prev_row[j] if j < len(prev_row) else 0
        y = prev_row[j-1] if j-1 >= 0 else 0
        row[j] = x + y
    else:
      triangle[i][0] += 1
  return triangle

print(pascal_triangle(6))
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
