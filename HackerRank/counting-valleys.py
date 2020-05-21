# Counting Valleys #

# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like
# topography. During his last hike, he took exactly steps. For every step he took, he noted if it was an uphill
# or a downhill step. Gary's hikes start and end at sea level. We define the following terms:

#   A mountain is a non-empty sequence of consecutive steps above sea level, starting with a step up from
#       sea level and ending with a step down to sea level.
#   A valley is a non-empty sequence of consecutive steps below sea level, starting with a step down from
#       sea level and ending with a step up to sea level.

# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he
# walked through.

# Complete the countingValleys function below.


def countingValleys(n, s):
    level, valleys = 0, 0
    for step in s:
        if level is 0 and step is 'D':
            valleys += 1
        if step is 'D':
            level -= 1
        if step is 'U':
            level += 1
    return valleys


if __name__ == '__main__':
    print(countingValleys(8, 'UDDDUDUU'), 1)
    print(countingValleys(12, 'DDUUDDUDUUUD'), 2)
