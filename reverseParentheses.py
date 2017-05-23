import re

def reverseParentheses(s):

    # make a lsit of all open parenthesis indices
    open_indices = []
    for match in re.finditer('\(', ab):
        open_indices.append(match.start())

    print open_indices
    # loop this for each parenthetical:
        # get the innermost parenthetical
            # the innermost is the open parenthesis with the largest index
                # find all open parenthesis indices
                # make a list of these parenthesis
                # find the largest value in this list
                    # reverse it
        # get the next parenthetical (outward)


ab = 'hi (jann(el)le) bye'
reverseParentheses(ab)