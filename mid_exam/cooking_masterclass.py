from math import ceil

budget = float(input())
students = int(input())
package_of_flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

free_packages = students // 5
flour_price = package_of_flour_price * (students - free_packages)
eggs_price = single_egg_price * 10 * students
aprons_price = (single_apron_price * ceil(students + (students * 0.2)))
total_price = flour_price + eggs_price + aprons_price

difference = total_price - budget
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{difference:.2f}$ more needed.")
