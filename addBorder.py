'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''

def addBorder(picture):

    star_count = len(picture[0])
    add_layer(0, picture, star_count)

    # add left and right borders to each row
    for i in range(1, len(picture)):
        wrap_row(i, picture)

    add_layer(len(picture), picture, star_count)

    return picture


def add_layer(row, picture, star_count):

    picture.insert(row, (star_count + 2) * '*')
    return picture


def wrap_row(row, picture):
    picture[row] = "*" + picture[row] + "*"
    return picture

x = ['hi', 'to', 'hi']
addBorder(x)
print x