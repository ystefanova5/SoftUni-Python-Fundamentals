companies = {}
command = input()
while command != "End":
    current_company = command.split(" -> ")[0]
    current_id = command.split(" -> ")[1]
    if current_company not in companies:
        companies[current_company] = []
    if current_id not in companies[current_company]:
        companies[current_company].append(current_id)
    command = input()
for company in companies:
    print(company)
    for id in companies[company]:
        print(f"-- {id}")


################################################   Task Description   ################################################
# 10. Company Users
# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# • Until you receive the "End" command, you will be receiving input in the format:
#   "{company_name} -> {employee_id}".
# • The input always will be valid.
