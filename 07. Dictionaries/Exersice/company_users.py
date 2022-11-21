company_employees = {}
while True:
    command = input()
    if command == "End":
        break
    company, employee = command.split(" -> ")
    if company not in company_employees:
        company_employees[company] = []
    if employee in company_employees[company]:
        continue
    company_employees[company].append(employee)
for comp in company_employees:
    print(comp)
    for id in company_employees[comp]:
        print(f"-- {id}")
