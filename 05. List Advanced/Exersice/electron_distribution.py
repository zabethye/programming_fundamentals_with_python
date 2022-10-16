number_of_electrons = int(input())
electron = []
shell = 1

while number_of_electrons > 0:
    current_electron = 2 * shell ** 2
    shell += 1
    if number_of_electrons - current_electron >= 0:
        number_of_electrons -= current_electron
    else:
        current_electron = number_of_electrons
        number_of_electrons = 0
    electron.append(current_electron)

print(electron)