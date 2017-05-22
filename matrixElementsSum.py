def matrixElementsSum(matrix):

    j = 0
    for row in matrix[1:]:

        i = 0
        for element in row:

            if matrix[j][i] == 0:
                matrix[j + 1][i] = 0
            i = i + 1

        j += 1

    return sum([sum(l) for l in matrix])