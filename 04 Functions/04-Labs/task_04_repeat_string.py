input_string = input()
num_repetitions = int(input())
result = lambda string, repetitions: string * repetitions
print(result(input_string, num_repetitions))


################################################   Task Description   ################################################
# 4. Repeat String
# Write a function that receives a string and a counter n. 
# The function should return a new string – the result of repeating the old string n times. 
# Print the result of the function. Try using lambda.
