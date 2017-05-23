import re

def reverseParentheses(s):

    # make a list of all open parenthesis indices
    open_indices = sorted(get_indices('\(', s), reverse=True)
    close_indices = get_indices('\)', s)

    for i in range(0, len(open_indices)):
        print s[open_indices[i] + 1:close_indices[i]]

    # loop this for each parenthetical:
        # get the innermost parenthetical
            # the innermost is the open parenthesis with the largest index
                # find all open parenthesis indices
                # make a list of these parenthesis
                # find the largest value in this list
                    # reverse it
        # get the next parenthetical (outward)


def get_indices(delimiter, str):

    indices_list = []
    for match in re.finditer(delimiter, str):
        indices_list.append(match.start())

    return indices_list

ab = 'hi (jann(el)le) bye'
reverseParentheses(ab)