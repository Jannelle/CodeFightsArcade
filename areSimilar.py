'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
'''

def areSimilar(a, b):
    # in order for two arrays to be similar, they must have the same elements
    if not have_same_elements: return false
    # check they have the same elements
    # map each element to their index
    # compare each element and their indexes between the two arrays
    # if there are more than two mismatching index, they are not similar
    # if there are two mismatching indexes, see if they can be swapped

