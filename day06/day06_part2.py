with open('day06_input.txt') as f:
    orbits = f.readlines()
orbits = [x.strip('\n') for x in orbits]

example1 = 'COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L'.split(' ')
example2 = 'COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L K)YOU I)SAN'.split(' ')

planet_connections = {}
visited_planets = {}
path_to_santa = []


def populate_connections(all_orbits):
	for orbit in all_orbits:
		parent_planet = orbit.split(')')[0]
		orbiter = orbit.split(')')[1]

		if parent_planet not in planet_connections:
			planet_connections[parent_planet] = set()
		planet_connections[parent_planet].add(orbiter)

		if orbiter not in planet_connections:
			planet_connections[orbiter] = set()
		planet_connections[orbiter].add(parent_planet)

		if parent_planet not in visited_planets:
			visited_planets[parent_planet] = False
		if orbiter not in visited_planets:
			visited_planets[orbiter] = False
	return planet_connections


def find_path(com, destination, visited_planets, path):
	visited_planets[com] = True
	path.append(com)

	if com == destination:
		print("Path", path)
		# orbit_counts.append(len(path)-1)
		path_to_santa.extend(path)
	else:
		for p in planet_connections[com]:
			if visited_planets[p] == False:
				find_path(p, destination, visited_planets, path)

	path.pop()
	visited_planets[com] = False


def calulate_orbits(com, planet_connections, visited_planets):
	total_orbits = 0
	for planet in visited_planets.keys():
		find_path(com, planet, visited_planets, [])
	total_orbits = sum(orbit_counts)
	return total_orbits


def calculate_orbital_transfers(path):
	return len(path)-3


populate_connections(orbits)

print(find_path('YOU', 'SAN', visited_planets, []))
print(calculate_orbital_transfers(path_to_santa))

