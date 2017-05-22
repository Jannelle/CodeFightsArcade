def matrixElementsSum(matrix):
    pass
    # loop through each matrix from the 2nd row on
    j = 0
    for row in matrix[1:]:

        i = 0
        for element in row:

            print element, matrix[j][i]
            i = i + 1

        j += 1

    # loop through each element in the matrix
    # if the element at the same index from the previous row is 0, make this element 0
    # get the sum of each row


# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]

matrix = [['1_1', '1_2', '1_3', '1_4'],
          ['2_1', '2_2', '2_3', '2_4'],
          ['3_1', '3_2', '3_3', '3_4']]

print matrixElementsSum(matrix)