def matrixElementsSum(matrix):
    pass
    # loop through each matrix from the 2nd row on
    j = 0
    for row in matrix[1:]:

        i = 0
        for element in row:

            if matrix[j][i] == 0:
                matrix[j + 1][i] = 0
            i = i + 1

        j += 1

    print sum([sum(l) for l in matrix])


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

print matrixElementsSum(matrix)