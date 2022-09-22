year = int(input())
happy_year_occurred = False
next_year = year

while not happy_year_occurred:
    next_year += 1
    digits = set()
    for char in str(next_year):
        digits.add(int(char))
    happy_year_occurred = len(digits) == len(str(year))

print(next_year)
