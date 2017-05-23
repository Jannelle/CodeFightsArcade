import re

def reverseParentheses(s):

    # reverse open_indices so that the innermost goes first
    open_indices = sorted(get_indices('\(', s), reverse=True)

    new_string = s
    for i in range(0, len(open_indices)):
        # this is the phrase to reverse
        reversed_string = to_reverse(open_indices[i],new_string)[::-1]

        # save the strings before and after the parentheses to pre/append later
        first_part = new_string[:open_indices[i]]
        last_part = new_string[open_indices[i] + len(reversed_string) + 2:] #+2 for the closed parenthesis

        new_string = first_part + '(' + reversed_string + ')' + last_part

    return new_string.replace('(', '').replace(')', '')

def get_indices(delimiter, str):

    indices_list = []
    for match in re.finditer(delimiter, str):
        indices_list.append(match.start())

    return indices_list


def to_reverse(open, str):
    # from the given open parenthesis to the first closed parenthesis
    closed_index = str.index(')', open)
    phrase = str[open + 1:closed_index]

    # we need to make sure there's enough closed parenthesis to covered the open
    while phrase.count('(') >= phrase.count(')'):
        phrase += str[closed_index]
        closed_index += 1

    return phrase[:-1]

x = 'I(CU(VE(RE)UV)OY)YM)OL)H'
print reverseParentheses(x)

