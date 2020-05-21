# Juming on the Clouds #

# Emma is playing a new mobile game involving n clouds numbered 0 from to n-1. A player initially starts
# out on cloud 0, and they must jump to cloud n-1. In each step, she can jump from any cloud i to cloud
# i+1 or cloud i+2.

# There are two types of clouds, ordinary clouds and thunderclouds. The game ends if Emma jumps onto a
# thundercloud, but if she reaches the last cloud (i.e., n-1), she wins the game! Assume their will
# always be a way to win.


def jumpingOnClouds(c):
    index, jumps = 0, 0
    while index < len(c):
        if index+2 < len(c) and c[index+2] is not 1:
            jumps += 1
            index += 2
        elif index+1 < len(c) and c[index+1] is not 1:
            jumps += 1
            index += 1
        else:
            index += 1
    return jumps


if __name__ == '__main__':
    print(jumpingOnClouds(7, [0, 0, 1, 0, 0, 1, 0]), 4)
    print(jumpingOnClouds(6, [0, 0, 0, 1, 0, 0]), 3)
