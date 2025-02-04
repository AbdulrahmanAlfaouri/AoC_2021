with open("input.txt") as f:
    in_text = f.readlines()

in_numbers = [line.strip() for line in in_text]
hight_map = [[j for j in i] for i in in_numbers]


def get_low_points(hight_map):
    low_points = []
    for numi, i in enumerate(hight_map):
        for numj, j in enumerate(i):
            adjecent = []
            try:
                up = hight_map[numi - 1][numj]
                adjecent.append(up)
            except IndexError:
                pass

            try:
                down = hight_map[numi + 1][numj]
                adjecent.append(down)
            except IndexError:
                pass

            try:
                left = hight_map[numi][numj - 1]
                adjecent.append(left)
            except IndexError:
                pass

            try:
                right = hight_map[numi][numj + 1]
                adjecent.append(right)
            except IndexError:
                pass

            if all(j < num for num in adjecent):
                low_points.append([numi, numj])
    return low_points


def get_basins_score(low_points, hight_map):
    basins_lenghs = []
    for low_point in low_points:
        points = [low_point]

        for j in points:
            y = j[0]
            x = j[1]

            hight_map[y][x] = "a"
            # up
            if y != len(hight_map) - 1:
                if hight_map[y + 1][x] != "9" and hight_map[y + 1][x] != "a":

                    if [y + 1, x] not in points:
                        points.append([y + 1, x])
            # down
            if y != 0:
                if hight_map[y - 1][x] != "9" and hight_map[y - 1][x] != "a":

                    if [y - 1, x] not in points:
                        points.append([y - 1, x])
            # left
            if x != 0:
                if hight_map[y][x - 1] != "9" and hight_map[y][x - 1] != "a":

                    if [y, x - 1] not in points:
                        points.append([y, x - 1])
            # right
            if x != len(hight_map[0]) - 1:
                if hight_map[y][x + 1] != "9" and hight_map[y][x + 1] != "a":

                    if [y, x + 1] not in points:
                        points.append([y, x + 1])

        basins_lenghs.append(len(points))

    basins_lenghs.sort()
    final_score = basins_lenghs[-1] * basins_lenghs[-2] * basins_lenghs[-3]
    return final_score


low_points = get_low_points(hight_map)
score = get_basins_score(low_points, hight_map)
print(score)
