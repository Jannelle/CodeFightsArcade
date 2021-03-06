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
    for i in range(0, len(inputArray) - 1):
        if inputArray[i] >= inputArray[i + 1]:
            diff = inputArray[i] - inputArray[i + 1] + 1
            inputArray[i + 1] = inputArray[i] + 1
            count += diff

    return count

x = [1, 1, 1]
print arrayChange(x)