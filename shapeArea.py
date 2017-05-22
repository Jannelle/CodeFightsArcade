def shapeArea(n):
    area = 1
    multiplier = 0
    for x in range(1, n + 1):
        area = (2 * multiplier) + area
        multiplier += 2
    return area
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

