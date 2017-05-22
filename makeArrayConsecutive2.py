def makeArrayConsecutive2(statues):
    statues.sort()

    biggest = max(statues)
    smallest = min(statues)

    i = smallest
    new_count = 0
    for x in range(smallest, biggest):
        i += 1
        if not i in statues:
            new_count += 1

    return new_count
