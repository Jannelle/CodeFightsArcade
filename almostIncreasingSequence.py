def almostIncreasingSequence(sequence):
    remove_count = 0

    for i in range(0, len(sequence) - 1):
        num1 = sequence[i]
        num2 = sequence[i + 1]

        if not isIncreasing(num1, num2):
            if remove_count == 0:
                remove_count = 1
                if not test1(i, sequence) and not test2(i + 1, sequence):
                    return False
            elif remove_count > 0:
                return False

    return True


def isIncreasing(num1, num2):
    if num2 > num1:
        return True


def test1(i, sequence):
    if i > 0:

        num1 = sequence[i - 1]
        num2 = sequence[i + 1]
        if isIncreasing(num1, num2):
            return True
        else:
            return False
    else:
        return True


def test2(i, sequence):
    if i < len(sequence) - 1:
        num1 = sequence[i - 1]
        num2 = sequence[i + 1]
        if isIncreasing(num1, num2):
            return True
        else:
            return False
    return True