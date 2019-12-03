
import operator

with open('/Users/yih/Desktop/Home/advent-of-code/day02/day02_input.txt') as f:
    op_codes = f.readlines()

op_codes = map(int, op_codes[0].split(','))

opcodes = {
	1: operator.add,
	2: operator.mul
}

target = 19690720

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
				# print("We're done")
				return op_codes[0]
			else:
				print("Unknown op code")
				return op_codes


def program_1202(op_codes, noun, verb):
	# copy op_codes
	trial_op_codes = op_codes[:]
	# replace position 1 with noun
	trial_op_codes[1] = noun
	# replace postion 2 with verb
	trial_op_codes[2] = verb

	return process_opcodes(trial_op_codes)


def get_noun_verb_combo(op_codes):
	# maybe this could be better
	for noun in range(0, 100):
		for verb in range(0, 100):
			output = program_1202(op_codes, noun, verb)
			if output == target:
				return noun, verb
	return "No such combo"


print(get_noun_verb_combo(op_codes))



