input_string = input()
shuffles_count = int(input())
original_list = input_string.split(" ")
middle = int(len(original_list) / 2)
shuffled_string = original_list
for shuffle in range(shuffles_count):
    first_list = shuffled_string[0:middle]
    second_list = shuffled_string[middle:]
    shuffled_string = []
    for i in range(len(first_list)):
        shuffled_string.append(first_list[i])
        shuffled_string.append(second_list[i])
print(shuffled_string)


################################################   Task Description   ################################################
# 5. Faro Shuffle
# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. 
# Then the cards in the two halves are perfectly interleaved, 
# such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, 
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) 
# and on the second line receives a count of faro shuffles that should be made. 
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.
