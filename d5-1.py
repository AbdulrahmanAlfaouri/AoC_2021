with open('input.txt') as in_text:
    line_segments = (''.join(in_text.readlines())).split('\n')


digram = [[] for i in range(1000)]

for num,list in enumerate(digram):
    digram[num] = ['.' for j in range(1000)]

def update_diagram(all_points):
    for point in all_points:
        x = point[0]
        y = point[1]

        if digram[x][y] == '.':
            # noinspection PyTypeChecker
            digram[x][y] = 1
        else:
            digram[x][y] += 1


for line_segment in line_segments:
    segment = line_segment.split('->')

    x1, y1 = segment[0].split(',')
    x2, y2 = segment[1].split(',')
    x1, y1 = int(x1),int(y1)
    x2, y2 = int(x2), int(y2)


    if y1 == y2:
        if x2>x1:
            xpoints = [point for point in range(x1,x2+1)]
            all_points = [[xpoynt,y1] for xpoynt in xpoints]
            update_diagram(all_points)
        else:
            xpoints = [point for point in range(x2,x1+1)]
            all_points = [[xpoynt,y1] for xpoynt in xpoints]

            update_diagram(all_points)

    elif x1 == x2:
        if y2>y1:
            ypoints = [ypoint for ypoint in range(y1,y2+1)]
            all_points = [[x1, ypoynt] for ypoynt in ypoints]
            update_diagram(all_points)
        else:
            ypoints = [ypoint for ypoint in range(y2,y1+1)]
            all_points = [[x1, ypoynt] for ypoynt in ypoints]
            update_diagram(all_points)
    else:
        ypoints = [ypoint for ypoint in range(y1, y2+1)] if y2>y1 else [ypoint for ypoint in range(y2, y1+1)]
        xpoints = [point for point in range(x1,x2+1)] if x2>x1 else [point for point in range(x2,x1+1)]

        if x1>x2:
            xpoints.reverse()
        if y1>y2:
            ypoints.reverse()

        all_points = [[xpoint, ypoint] for xpoint, ypoint in zip(xpoints, ypoints)]
        update_diagram(all_points)




overlaps = 0
digram_as_alist = [cell for sublist in digram for cell in sublist]

for num in digram_as_alist:
    if num != '.' and num >= 2:
        overlaps += 1

print(overlaps)




