
my_moons = [
[-17,9,-5],
[-1,7,13],
[-19,12,5],
[-6,-6,-4]
]

# positions = []
velocities = [[0 for x in range(0,3)] for y in range(0,4)]


def populate_positions(positions, velocities):
	# apply gravity
	for i, moon in enumerate(positions):
		for x, other_moon in enumerate(positions):
			if i != x:
				for n, coordinate in enumerate(moon):
					if moon[n] == other_moon[n]:
						continue
					if moon[n] < other_moon[n]:
						velocities[i][n] += 1
					else:
						velocities[i][n] -= 1

	# apply velocity
	for i, moon in enumerate(positions):
		for t, coord in enumerate(moon):
			positions[i][t] = moon[t] + velocities[i][t]

	return positions, velocities


def run_steps(steps, positions, velocities):
	iteration = 0
	while(iteration < steps):
		print("Step", iteration, "positions", positions, "velocities", velocities)
		total_nrg = calc_total_nrg_all_moons(positions, velocities)
		positions, velocities = populate_positions(positions, velocities)
		print("total_nrg", total_nrg)
		iteration += 1
	return "End of simulation"


def calculate_energy(coordinates):
	return sum(map(abs, coordinates))


def calculate_total_energy(moon, velocity):
	potential_nrg = calculate_energy(moon)
	kinetic_nrg = calculate_energy(velocity)
	return potential_nrg * kinetic_nrg


def calc_total_nrg_all_moons(positions, velocities):
	total_system_nrg = 0
	for i, moon in enumerate(positions):
		total_nrg = calculate_total_energy(moon, velocities[i])
		total_system_nrg += total_nrg
	return total_system_nrg


example1 = [[-1,0,2], [2,-10,-7], [4,-8,8], [3,5,-1]]
example2 = [[-8,-10,0], [5,5,10], [2,-7,3], [9,-8,-3]]

run_steps(1001, my_moons, velocities)

