with open('input.txt') as in_text:
    in_numbers = in_text.readline().split(',')
    in_numbers = [int(num) for num in in_numbers]


all_of_the_really_shits = []

for i in range(min(in_numbers), max(in_numbers)):
    print(f'using i = {i}')
    really_shit = 0
    for hehe in in_numbers:
        shit = 0
        full_shit = 0
        m = 0
        shit += abs(i-hehe)
        for pshit in range(shit+1):
            full_shit += pshit

        really_shit += full_shit



    all_of_the_really_shits.append(really_shit)

try:
    print(min(all_of_the_really_shits))
except ValueError:
    print('shit')

