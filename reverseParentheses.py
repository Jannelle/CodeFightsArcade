import re

def reverseParentheses(s):

    # reverse open_indices so that the innermost goes first
    open_indices = sorted(get_indices('\(', s), reverse=True)
    closed_indices = get_indices('\)', s)

    for i in range(0, len(open_indices)):
        # save the strings before and after the parentheses to pre/append later
        first_part = s[:open_indices[i]]
        last_part = s[closed_indices[i] + 1 :]

        # this is the phrase to reverse
        to_reverse = s[open_indices[i] + 1:closed_indices[i]]
        reversed_string = '(' + to_reverse[::-1] + ')'

        s = first_part + reversed_string + last_part

    print s

def get_indices(delimiter, str):

    indices_list = []
    for match in re.finditer(delimiter, str):
        indices_list.append(match.start())

    return indices_list

ab = 'hi (jann(el)le) bye'
reverseParentheses(ab)