with open('input.txt') as in_text:
    in_numbers = in_text.readline().split(',')
    in_numbers = [int(num) for num in in_numbers]


all_fuel_needed = []

for i in range(min(in_numbers), max(in_numbers)):
    print(f'using i = {i}')
    fuel_needed = 0
    for pos_num in in_numbers:
        fuel_needed_for_pos = 0
        fuel_sum_for_all_steps = 0

        fuel_needed_for_pos += abs(i - pos_num)
        for pos_step in range(fuel_needed_for_pos + 1):
            fuel_sum_for_all_steps += pos_step

        fuel_needed += fuel_sum_for_all_steps



    all_fuel_needed.append(fuel_needed)

try:
    print(min(all_fuel_needed))
except ValueError:
    print('all fuel needed is [] -_-')

