
import operator

with open('/Users/yih/Desktop/Home/advent-of-code/day02/day02_input.txt') as f:
    op_codes = f.readlines()

op_codes = map(int, op_codes[0].split(','))

opcodes = {
	1: operator.add,
	2: operator.mul
}

def process_opcodes(op_codes):
	index = 0
	while(index < len(op_codes)):
		op_code = op_codes[index]
		if op_code in opcodes:
			val1_pos = op_codes[index+1]
			val2_pos = op_codes[index+2]
			calc_val = opcodes[op_code](op_codes[val1_pos], op_codes[val2_pos])
			calc_val_pos = op_codes[index+3]
			op_codes[calc_val_pos] = calc_val
			index = index + 4
		else:
			if op_codes[index] == 99:
				print("We're done")
				return op_codes[0]
			else:
				print("Unknown op code")
				return op_codes


def program_1202(op_codes):
	# replace position 1 with 12
	op_codes[1] = 12
	# replace postion 2 with 2
	op_codes[2] = 2

	return process_opcodes(op_codes)


# example1 = map(int, "1,9,10,3,2,3,11,0,99,30,40,50".split(','))
# print(process_opcodes(example1))

# example2 = map(int, "1,0,0,0,99".split(','))
# print(process_opcodes(example2))

# example3 = map(int, "2,3,0,3,99".split(','))
# print(process_opcodes(example3))

# example4 = map(int, "2,4,4,5,99,0".split(','))
# print(process_opcodes(example4))

# example5 = map(int, "1,1,1,4,99,5,6,0,99".split(','))
# print(process_opcodes(example5))

print(program_1202(op_codes))



