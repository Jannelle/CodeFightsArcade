'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''
from itertools import cycle

def arrayChange(inputArray):

    count = 0
    # do this until it's strictly increasing
    while not is_increasing(inputArray):
        for i in range(0, len(inputArray) - 1):
            while inputArray[i] >= inputArray[i + 1]:
                inputArray[i + 1] += 1
                count += 1

    return count

def is_increasing(inputArray):
    # must be sorted and have no duplicates
    if inputArray == sorted(inputArray) and len(inputArray) == len(set(inputArray)):
        return True
    else:
        return False
