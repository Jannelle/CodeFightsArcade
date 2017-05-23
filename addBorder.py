def addBorder(picture):
    # add the top layer
    add_layer(0, picture)

    # add left and right borders to each row
    for row in picture:
        add_border(row)

    # add bottom layer
    add_layer(len(picture) - 1, picture)



def add_top_layer(row, picture):
    pass

def add_border(row, picture):
    pass