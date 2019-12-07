
import operator

with open('/Users/yih/Desktop/Home/advent-of-code/day05/day05_input.txt') as f:
    op_codes = f.readlines()

op_codes = map(int, op_codes[0].split(','))

opcodes = {
	1: operator.add,
	2: operator.mul,
}


def process_opcodes(op_codes, input_value):
	index = 0
	while(index < len(op_codes)):
		op_code = op_codes[index]
		# print("current op code", op_code, "index", index)
		if op_code in opcodes:
			val1_pos = op_codes[index+1]
			val2_pos = op_codes[index+2]
			calc_val = opcodes[op_code](op_codes[val1_pos], op_codes[val2_pos])
			calc_val_pos = op_codes[index+3]

			# print("saving", calc_val, "to", calc_val_pos)

			op_codes[calc_val_pos] = calc_val
			index = index + 4
		# add instructions for new op codes
		elif op_code == 3:
			parameter = op_codes[index+1]
			# print("saving", input_value, "to", parameter)
			op_codes[parameter] = input_value
			index = index + 2
		elif op_code == 4:
			parameter = op_codes[index+1]
			print("Test result", op_codes[parameter])
			index = index + 2
		elif op_code > 99:
			actual_opcode = int(str(op_code)[-2:])
			# print("actual_opcode", actual_opcode)

			parameter_modes = str(op_code)[:len(str(op_code))-2][::-1]
			parameter1 = 0 
			parameter2 = 0
			parameter3 = 0

			if len(parameter_modes) > 0:
				parameter1 = int(parameter_modes[0])
			if len(parameter_modes) > 1:
				parameter2 = int(parameter_modes[1])
			if len(parameter_modes) > 2:
				parameter3 = int(parameter_modes[2])

			if actual_opcode in opcodes:
				val1_pos = op_codes[index+1]
				val2_pos = op_codes[index+2]

				val1 = op_codes[val1_pos] if parameter1 == 0 else op_codes[index+1]
				val2 = op_codes[val2_pos] if parameter2 == 0 else op_codes[index+2]

				calc_val = opcodes[actual_opcode](val1, val2)
				calc_val_pos = op_codes[index+3]

				if parameter3 == 0:
					# print("saving", calc_val, "to", calc_val_pos)
					op_codes[calc_val_pos] = calc_val
				else:
					print(calc_val)
				index = index + 4
			else:
				if actual_opcode == 4:
					parameter = op_codes[index+1]
					if parameter1 == 0:
						print("Test result", opcodes[parameter])
					else:
						print("Test result", parameter)
					index = index + 2
				else:
					parameter = op_codes[index+1]
					# print("saving", input_value, "to", parameter)
					op_codes[parameter] = input_value
					index = index + 2
		else:
			if op_codes[index] == 99:
				print("We're done")
				return input_value
			else:
				print("Unknown op code")
				return op_codes


example1 = [3,0,4,0,99]
example2 = [1002,4,3,4,33]
example3 = [1101,100,-1,4,0]

print(process_opcodes(op_codes, 1))












