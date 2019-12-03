
import sys

with open('/Users/yih/Desktop/Home/advent-of-code/day03/day03_input.txt') as f:
    coordinates = f.readlines()

# puzzle input
puzzle_wire1 = coordinates[0]
puzzle_wire2 = coordinates[1]

# min distance should be 6
# min steps should be 30
example1_wire1 = 'R8,U5,L5,D3'
example1_wire2 = 'U7,R6,D4,L4'

# min distance should be 159
# min steps should be 610
example2_wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
example2_wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# min distance should be 135
# min steps should be 410
example3_wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
example3_wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

# x coordinates with y coordinates in sets
wire1_xcoord = {}
wire2_xcoord = {}

cross_locations = {}
origin_point = [0,0]

steps_to_intersections_wire1 = {}
steps_to_intersections_wire2 = {}


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
					if x not in cross_locations:
						cross_locations[x] = set()
					cross_locations[x].add(y)
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


def populate_steps_to_instersections(wire, cross_points, steps_to_intersections_wire):
	wire_directions = wire.split(',')
	current_coord = [0,0]
	steps = 0
	for d in wire_directions:
		units = int(d[1:])
		if d[0] == 'R':
			for u in range(0, units):
				current_coord[0] += 1
				steps += 1
				if current_coord[0] in cross_points:
					if current_coord[1] in cross_points[current_coord[0]]:
						cross_point = current_coord
						if str(cross_point) not in steps_to_intersections_wire:
							steps_to_intersections_wire[str(cross_point)] = steps
		if d[0] == 'U':
			for u in range(0, units):
				current_coord[1] += 1
				steps += 1
				if current_coord[0] in cross_points:
					if current_coord[1] in cross_points[current_coord[0]]:
						cross_point = current_coord
						if str(cross_point) not in steps_to_intersections_wire:
							steps_to_intersections_wire[str(cross_point)] = steps
		if d[0] == 'D':
			for u in range(0, units):
				current_coord[1] -= 1
				steps += 1
				if current_coord[0] in cross_points:
					if current_coord[1] in cross_points[current_coord[0]]:
						cross_point = current_coord
						if str(cross_point) not in steps_to_intersections_wire:
							steps_to_intersections_wire[str(cross_point)] = steps
		if d[0] == 'L':
			for u in range(0, units):
				current_coord[0] -= 1
				steps += 1
				if current_coord[0] in cross_points:
					if current_coord[1] in cross_points[current_coord[0]]:
						cross_point = current_coord
						if str(cross_point) not in steps_to_intersections_wire:
							steps_to_intersections_wire[str(cross_point)] = steps
	return current_coord


def calc_min_steps(steps_wire1, steps_wire2):
	min_steps = sys.maxint
	for cross_point in steps_wire1:
		total_steps = steps_wire1[cross_point] + steps_wire2[cross_point]
		if total_steps < min_steps:
			min_steps = total_steps
	return min_steps


populate_wire_coordinates(puzzle_wire1, wire1_xcoord)
populate_wire_coordinates(puzzle_wire2, wire2_xcoord)

get_cross_locations(wire1_xcoord, wire2_xcoord)
populate_steps_to_instersections(puzzle_wire1, cross_locations, steps_to_intersections_wire1)
populate_steps_to_instersections(puzzle_wire2, cross_locations, steps_to_intersections_wire2)

print(calc_min_steps(steps_to_intersections_wire1, steps_to_intersections_wire2))










