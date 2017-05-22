def allLongestStrings(inputArray):
    # find the longest string
    max_string = max(len(x) for x in inputArray)

    longest_strings =[]
    for str in inputArray:
        if len(str) == max_string:
            longest_strings.append(str)

    return longest_strings