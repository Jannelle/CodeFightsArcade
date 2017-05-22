def allLongestStrings(inputArray):
    # find the longest string
    max_string = max(len(x) for x in array)

    count = 0
    for str in inputArray:
        if len(str) == max_string:
            count += 1

    return count