
import sys
from decimal import *
from math import *

with open('day10_input.txt') as f:
    grid = f.readlines()

grid = [x.strip('\n') for x in grid]
# print(grid)

coordinates = {}
lines_of_sight = {}
# epsilon = sys.float_info.epsilon 
epsilon = 0.00001


def populate_coordinates(asteroid_grid, coordinates):
	asteroid = 0
	for i, x in enumerate(asteroid_grid):
		for y in range(len(x)):
			if x[y] == '#':
				coordinates[asteroid] = [y, i]
				asteroid += 1
	return coordinates


def get_line_of_sight(coordinate1, coordinate2):
	rise = Decimal(coordinate2[1] - coordinate1[1])
	run = Decimal(coordinate2[0] - coordinate1[0])
	# print("rise", rise, "run", run)
	slope = 0

	if -1 * epsilon < run and run < epsilon:
		slope = sys.maxint
	else:
		slope = rise / run
	return slope


def populate_lines_of_sight(coordinates, lines_of_sight):
	getcontext().prec = 4
	for asteroid in coordinates:
		for other_asteroid in coordinates:
			if asteroid != other_asteroid:
				# print("asteroid", asteroid, "other_asteroid", other_asteroid)
				line_of_sight = get_line_of_sight(coordinates[asteroid], coordinates[other_asteroid])
				if asteroid not in lines_of_sight:
					lines_of_sight[asteroid] = {}
				if line_of_sight not in lines_of_sight[asteroid]:
					lines_of_sight[asteroid][line_of_sight] = [other_asteroid]
				else:
					if len(lines_of_sight[asteroid][line_of_sight]) < 2:
						existing_asteroid = lines_of_sight[asteroid][line_of_sight][0]
						if is_between(coordinates[other_asteroid], coordinates[asteroid], coordinates[existing_asteroid]):
							lines_of_sight[asteroid][line_of_sight].append(other_asteroid)
	return lines_of_sight


def distance(asteroid1, asteroid2):
	return sqrt((asteroid1[0] - asteroid2[0])**2 + (asteroid1[1] - asteroid2[1])**2)


def is_between(asteroid1, asteroid3, asteroid2):
	distance_delta = distance(asteroid1, asteroid3) + distance(asteroid3, asteroid2) - distance(asteroid1, asteroid2)
	# print("distance_delta", distance_delta, -1 * epsilon < distance_delta and distance_delta < epsilon)
	return -1 * epsilon < distance_delta and distance_delta < epsilon


def get_max_asteroid_count(lines_of_sight):
	max_count = -sys.maxint
	asteroid_max = None
	for asteroid in lines_of_sight:
		curr_count = 0
		for line in lines_of_sight[asteroid]:
			curr_count += len(lines_of_sight[asteroid][line])
			# print("asteroid", asteroid, lines_of_sight[asteroid][line], len(lines_of_sight[asteroid][line]))
		if curr_count > max_count:
			max_count = curr_count
			asteroid_max = asteroid
			print(asteroid, max_count)
	return max_count


# should be 8
example1 = ['.#..#','.....','#####','....#','...##'] 
# should be 33
example2 = ['......#.#.','#..#.#....','..#######.','.#.#.###..','.#..#.....','..#....#.#','#..#....#.','.##.#..###','##...#..#.','.#....####']
# should be 35
example3 = ['#.#...#.#.','.###....#.','.#....#...','##.#.#.#.#','....#.#.#.','.##..###.#','..#...##..','..##....##','......#...','.####.###.']
# should be 41
example4 = ['.#..#..###','####.###.#','....###.#.','..###.##.#','##.##.#.#.','....###..#','..#.#..#.#','#..#.#.###','.##...##.#','.....#.#..']
# should be 210
example5 = ['.#..##.###...#######',
'##.############..##.',
'.#.######.########.#',
'.###.#######.####.#.',
'#####.##.#.##.###.##',
'..#####..#.#########',
'####################',
'#.####....###.#.#.##',
'##.#################',
'#####.##.###..####..',
'..######..##.#######',
'####.##.####...##..#',
'.#####..#.######.###',
'##...#.##########...',
'#.##########.#######',
'.####.#.###.###.#.##',
'....##.##.###..#####',
'.#.#.###########.###',
'#.#.#.#####.####.###',
'###.##.####.##.#..##']

# guessed 237, which is too low
# should be 284
populate_coordinates(grid, coordinates)
populate_lines_of_sight(coordinates, lines_of_sight)
print(get_max_asteroid_count(lines_of_sight))


