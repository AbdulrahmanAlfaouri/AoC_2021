import random

all_points = {'start':['A','b'], 'A':['c','b','end'], 'b':['d','A','end'], 'd':['b'], 'c':['A']}
paths = []


path = []
end = False
start = 'start'
path.append(start)
while not end:	
	if len(all_points[start]) != 0:
		next_step = random.choice(all_points[start])

		path.append(next_step)

		if next_step == 'end':
			end = True

		if next_step.islower() == True:
			for point in all_points:
				if next_step in all_points[point]:
					all_points[point].remove(next_step)
		start = next_step
	else:
		print(path)
		break

print(all_points)
