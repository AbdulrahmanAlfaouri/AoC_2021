import logging
import numpy
from logging import info
from itertools import permutations, product, combinations

logging.basicConfig(filename="test.txt", level=logging.INFO, format="%(message)s")

with open("input.txt") as text:
    in_text = [i.strip() for i in text.readlines()]
    in_text = [[int(i) for i in j] for j in in_text]

shifts_to_adjecent_points = list(product([-1, 1], repeat=2))
for i in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
    shifts_to_adjecent_points.append(i)

number_of_flashs = 0

def get_adjecent_points(line, in_line_posetion):
    for shift in shifts_to_adjecent_points:
        x, y = shift[1], shift[0]

        try:
            adjecent_point = (line+y, in_line_posetion+x)

            if adjecent_point[0] >= 0 and adjecent_point[1] >= 0:
                in_text[line+y][in_line_posetion+x] += 1
                adjecent_point_value = in_text[line+y][in_line_posetion+x]
                if adjecent_point_value > 9 and adjecent_point not in flashed:
                    flashed.append(adjecent_point)
        except IndexError:
            pass
            # print(f'{(current_adjecent_point)} is not a valid point')


step = 0
while True:
    flashed = []
    added_to = []
    for step_part in range(3):
        for line_num, line in enumerate(in_text):
            for number_posetion, num in enumerate(line):
                if step_part == 0:
                    in_text[line_num][number_posetion] += 1
                if step_part == 1:
                    if num > 9:
                        flash_posetion = (line_num, number_posetion)
                        if flash_posetion not in flashed:
                            flashed.append(flash_posetion)

    for flashed_point in flashed:
        get_adjecent_points(flashed_point[0], flashed_point[1])
        
    for flashed_point in flashed:
        number_of_flashs += 1
        in_text[flashed_point[0]][flashed_point[1]] = 0


    if all([number==0 for line in in_text for number in line]) == True:
        info(step+1)
        break

    step += 1