
import sys

with open('/Users/yih/Desktop/Home/advent-of-code/day03/day03_input.txt') as f:
    coordinates = f.readlines()

# puzzle input
puzzle_wire1 = coordinates[0]
puzzle_wire2 = coordinates[1]

# min distance should be 6
example1_wire1 = 'R8,U5,L5,D3'
example1_wire2 = 'U7,R6,D4,L4'

# min distance should be 159
example2_wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
example2_wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# min distance should be 135
example3_wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
example3_wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

# x coordinates with y coordinates in sets
wire1_xcoord = {}
wire2_xcoord = {}

cross_locations = []
origin_point = [0,0]

def populate_wire_coordinates(wire, wire_xcoord):
	wire_directions = wire.split(',')
	current_coord = [0,0]
	for d in wire_directions:
		units = int(d[1:])
		# print(units)
		if d[0] == 'R':
			for u in range(0, units):
				current_coord[0] += 1
				if current_coord[0] not in wire_xcoord:
					wire_xcoord[current_coord[0]] = set()
				wire_xcoord[current_coord[0]].add(current_coord[1])
		if d[0] == 'U':
			for u in range(0, units):
				current_coord[1] += 1
				if current_coord[0] not in wire_xcoord:
					wire_xcoord[current_coord[0]] = set()
				wire_xcoord[current_coord[0]].add(current_coord[1])
		if d[0] == 'D':
			for u in range(0, units):
				current_coord[1] -= 1
				if current_coord[0] not in wire_xcoord:
					wire_xcoord[current_coord[0]] = set()
				wire_xcoord[current_coord[0]].add(current_coord[1])
		if d[0] == 'L':
			for u in range(0, units):
				current_coord[0] -= 1
				if current_coord[0] not in wire_xcoord:
					wire_xcoord[current_coord[0]] = set()
				wire_xcoord[current_coord[0]].add(current_coord[1])
	return current_coord


def get_cross_locations(wire1x, wire2x):
	for x in wire1x:
		if x in wire2x:
			for y in wire2x[x]:
				if y in wire1x[x]:
					cross_locations.append([x, y])
	return cross_locations


def calc_manhattan_distance(origin, cross_point):
	return abs(origin[0] - cross_point[0]) + abs(origin[1] - cross_point[1])


def calc_min_distance(origin, cross_point_list):
	min_distance = sys.maxint
	for cross_point in cross_point_list:
		current_distance = calc_manhattan_distance(origin, cross_point)
		if current_distance < min_distance:
			min_distance = current_distance
	return min_distance


populate_wire_coordinates(puzzle_wire1, wire1_xcoord)
populate_wire_coordinates(puzzle_wire2, wire2_xcoord)

get_cross_locations(wire1_xcoord, wire2_xcoord)

print(calc_min_distance(origin_point, cross_locations))










