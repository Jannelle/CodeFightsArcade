def allLongestStrings(inputArray):
    # find the longest string
    longest_string = max(len(x) for x in array)
    print longest_string

    # loop through each string in the array
        # if the string's length matches the longest string, print it

array = ["aba", "aa", "ad", "vcd", "aba"]
print allLongestStrings(array)