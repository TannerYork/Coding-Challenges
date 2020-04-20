# Flatten Array form Exercism #
# Take a nested list and return a single flattened list with all values except nil/null.


def flatten_array(array):
    output = []
    flatten_array_recursion(array, output.append)
    return output


def flatten_array_recursion(array, func):
    for value in array:
        if type(value) is list:
            flatten_array_recursion(value, func)
        elif value is not None:
            func(value)


# Base Tests
print(flatten_array([1, [2, 3, None, 4], [None], 5]))  # [1,2,3,4,5]
print(flatten_array([1, [2, 3, 4, 5, 6, 7], 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Edge Case Testing
print(flatten_array([None, [[[None]]], None, None, [[None, None]]]))  # []
print(flatten_array([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]))
# [0, 2, 2, 3, 8, 100, -2]
