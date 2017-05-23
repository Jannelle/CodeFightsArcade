def sortByHeight(a):

    tree_positions = get_tree_positions(a)
    remove_trees(tree_positions, a)
    a.sort
    reinsert_trees(tree_positions, a)
    return a


def get_tree_positions(a):

    positions = []
    for i in range(0, len(a)):
        if a[i] == -1:
            positions.append(i)

    return positions


def remove_trees(tree_positions, park):

    for position in sorted(tree_positions, reverse=True):
        del park[position]


def reinsert_trees(treepositions, a):

    for i in treepositions:
        a.insert(i, -1)


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print sortByHeight(a)