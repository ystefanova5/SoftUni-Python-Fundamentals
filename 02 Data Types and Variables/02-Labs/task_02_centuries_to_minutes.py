centuries = int(input())
days_in_one_year = 365.2422
years = centuries * 100
days = int(years * days_in_one_year)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")


################################################   Task Description   ################################################
# 2. Centuries to Minutes
# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
