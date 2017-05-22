def adjacentElementsProduct(inputArray):
    largest_product = -200000000

    for j in range(0, len(inputArray) - 1):
        first = inputArray[j]
        second = inputArray[j + 1]
        product = first * second
        if product > largest_product:
            largest_product = product

    return largest_product
