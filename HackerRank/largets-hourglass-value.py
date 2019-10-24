# Highest Hourglass Value Problem from HackerRank.com #

# Given a n*n two dimensional array, find the lagest hourglass value in the array

def hourglass_value(array, x, y):
    top = array[y][x] + array[y][x+1] + array[y][x+2]
    middle = array[y+1][x+1]
    bottom = array[y+2][x] + array[y+2][x+1] + array[y+2][x+2]
    return top + middle + bottom

def highest_hourglass_value(array):
    x = 0
    y = 0
    values = []
    for y in range(0, len(array)-2):
        for x in range(0, len(array[y])-2):
            values.append(hourglass_value(array, x, y))
    # Can be replaced by built in max() function (thanks Ryan H.)
    return max(values)
    
array = [
        [1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]]
        
print(highest_hourglass_value(array))
    