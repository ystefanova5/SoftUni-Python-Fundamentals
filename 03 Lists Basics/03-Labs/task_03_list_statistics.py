number = int(input())
positives_list = []
negatives_list = []
for item in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives_list.append(current_number)
    else:
        negatives_list.append(current_number)
print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")


################################################   Task Description   ################################################
# 3. List Statistics
# On the first line, you will receive a number n. On the following n lines, you will receive integers. 
# You should create and print two lists:
#     • One with all the positives (including 0) numbers
#     • One with all the negatives numbers
# Finally, print the following message: 
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"
