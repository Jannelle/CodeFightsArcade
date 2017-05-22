def isLucky(n):

    ticket_list = [int(n) for n in str(n)]
    half = len(ticket_list) / 2
    first_half = ticket_list[:half]
    second_half = ticket_list[half:]

    return sum(first_half) == sum(second_half)

print isLucky(n)