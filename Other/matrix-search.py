# Matrix Search from CTI-ISP 2020 #

# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.


def matrix_search(matrix, target):
    if matrix[0][0] > target:
        return 0

    target_row_index = -1
    for i in range(len(matrix)):
        if matrix[i][0] == target:
            return 1
        if matrix[i][0] > target:
            target_row_index = i-1
            break

    if target_row_index == -1:
        for el in matrix[len(matrix)-1]:
            if el == target:
                return 1
        return 0
    else:
        for el in matrix[target_row_index]:
            if el == target:
                return 1
        return 0


if __name__ == '__main__':
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(matrix_search(matrix, 3), 1)
    print(matrix_search(matrix, 34), 1)
    print(matrix_search(matrix, 16), 1)
    print(matrix_search(matrix, 0), 0)
    print(matrix_search(matrix, 17), 0)
    print(matrix_search(matrix, 51), 0)
