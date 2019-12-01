
# Part 1 & 2

with open('/Users/yih/Desktop/Home/advent-of-code/day01/day01_input.txt') as f:
    fuel = f.readlines()

fuel = [x.strip() for x in fuel] 

def calc_mass(mass):
	return int(int(mass) / 3) - 2

def total_mass(mass_list):
	total = 0
	for mass in mass_list:
		curr_mass = calc_mass(mass)
		while(curr_mass > 0): 
			total += curr_mass
			curr_mass = calc_mass(curr_mass)
	return total

print(total_mass(fuel))



