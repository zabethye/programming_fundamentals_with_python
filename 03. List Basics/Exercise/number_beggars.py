list_of_sums = input().split(", ")
beggars_count = int(input())
beggars_income = []
starting_index = 0
while starting_index < beggars_count:
    beggar_sum = 0
    for current_beggar in range(starting_index, len(list_of_sums), beggars_count):
        beggar_sum += int(list_of_sums[current_beggar])
    beggars_income.append(beggar_sum)
    starting_index += 1
print(beggars_income)

