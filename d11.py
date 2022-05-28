import numpy as np
import logging
from logging import info
from itertools import product

logging.basicConfig(filename="test.txt", level=logging.INFO, format="%(message)s")

with open("input.txt") as text:
    in_text = [i.strip() for i in text.readlines()]
    points_list = np.array([[int(i) for i in j] for j in in_text])

shifts_to_adjecent_points = list(product([-1, 1], repeat=2))
for i in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
    shifts_to_adjecent_points.append(i)


def get_adjecent_points(in_line_posetion, line):
    x = in_line_posetion
    y = line

    for shift in shifts_to_adjecent_points:
        x_shift, y_shift = shift[0], shift[1]

        adjecent_point = (x + x_shift, y + y_shift)

        # to not get a negative index and end up on the other side of the list
        if adjecent_point[0] >= 0 and adjecent_point[1] >= 0:
            try:
                points_list[y + y_shift, x + x_shift] += 1
                adjecent_point_value = points_list[y + y_shift, x + x_shift]
                if adjecent_point_value > 9 and adjecent_point not in flashed:
                    flashed.append(adjecent_point)
            except IndexError:
                pass


def get_all_zeros_step():
    global flashed
    step = 0
    number_of_flashs = 0
    all_zeros = False
    while not all_zeros:
        flashed = []
        for step_part in range(2):
            for line_num, line in enumerate(points_list):
                for number_posetion, num in enumerate(line):
                    if step_part == 0:
                        points_list[line_num, number_posetion] += 1
                    if step_part == 1:
                        if num > 9:
                            flash_posetion = (number_posetion, line_num)
                            if flash_posetion not in flashed:
                                flashed.append(flash_posetion)

        for point in flashed:
            get_adjecent_points(point[0], point[1])

        for point in flashed:
            number_of_flashs += 1
            points_list[point[1], point[0]] = 0

        if np.all((points_list == 0)):
            return step + 1
        step += 1


theStep = get_all_zeros_step()
