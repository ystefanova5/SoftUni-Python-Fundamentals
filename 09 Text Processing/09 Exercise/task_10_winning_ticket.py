def check_ticket_side(ticket_side):
    uninterrupted_match_length = 0
    match_symbol = ""
    for symbol in ticket_side:
        if symbol != match_symbol:
            if uninterrupted_match_length >= 6:
                break
            uninterrupted_match_length = 1
            match_symbol = symbol
        else:
            uninterrupted_match_length += 1
    return uninterrupted_match_length, match_symbol


tickets = [x.strip() for x in input().split(", ")]
special_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if ticket[0] in special_symbols and ticket[0] * 20 == ticket:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        else:
            first_side = ticket[:10]
            second_side = ticket[10:]
            side_one_uninterrupted, side_one_symbol = check_ticket_side(first_side)
            side_two_uninterrupted, side_two_symbol = check_ticket_side(second_side)
            winning_length = min(side_one_uninterrupted, side_two_uninterrupted)
            if side_one_symbol == side_two_symbol and side_two_symbol in special_symbols and winning_length >= 6:
                print(f'ticket "{ticket}" - {winning_length}{side_one_symbol}')
            else:
                print(f'ticket "{ticket}" - no match')


#################################################   Task Description   ################################################
# 10. *Winning Ticket
# The lottery is exciting. However, checking a million tickets for winnings only by hand is not.
# So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:
# • A valid ticket has exactly 20 characters.
# • A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^'
#   uninterruptedly repeated at least 6 times in both halves of the tickets.
# • In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console.
# The input consists of a single line containing all tickets separated by commas
# and one or more white spaces in the format:
# • "{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# • If the ticket is invalid: "invalid ticket"
# • If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# • If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# • It the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
# Constrains
# • Number of tickets will be in range [0 … 100]
