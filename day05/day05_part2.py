
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
			print("Test result", op_codes[parameter], "using value", input_value)
			index = index + 2
		elif op_code == 5:
			if op_codes[op_codes[index+1]] != 0:
				index = op_codes[op_codes[index+2]]
			else:
				index = index + 3
		elif op_code == 6:
			# print("code 6", op_codes[index+1])
			if op_codes[op_codes[index+1]] == 0:
				index = op_codes[op_codes[index+2]]
			else:
				index = index + 3
		elif op_code == 7:
			if op_codes[op_codes[index+1]] < op_codes[op_codes[index+2]]:
				op_codes[op_codes[index+3]] = 1
			else:
				op_codes[op_codes[index+3]] = 0
			index = index + 4
		elif op_code == 8:
			if op_codes[op_codes[index+1]] == op_codes[op_codes[index+2]]:
				op_codes[op_codes[index+3]] = 1
			else:
				op_codes[op_codes[index+3]] = 0
			index = index + 4
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
						print("Test result", opcodes[parameter], "using value", input_value)
					else:
						print("Test result", parameter, "using value", input_value)
					index = index + 2
				elif actual_opcode == 3:
					parameter = op_codes[index+1]
					# print("saving", input_value, "to", parameter)
					op_codes[parameter] = input_value
					index = index + 2
				elif actual_opcode == 5:
					# print("code 5", parameter1, parameter2)
					first_param = op_codes[op_codes[index+1]] if parameter1 == 0 else op_codes[index+1]
					sec_param = op_codes[op_codes[index+2]] if parameter2 == 0 else op_codes[index+2]
					# print("code 5", first_param, sec_param)
					if first_param != 0:
						index = sec_param
					else:
						index = index + 3
				elif actual_opcode == 6:
					# print("code 6", parameter1, parameter2)
					first_param = op_codes[op_codes[index+1]] if parameter1 == 0 else op_codes[index+1]
					sec_param = op_codes[op_codes[index+2]] if parameter2 == 0 else op_codes[index+2]
					# print("code 6", first_param, sec_param)
					if first_param == 0:
						index = sec_param
					else:
						index = index + 3
				elif actual_opcode == 7:
					# print("code 7", parameter1, parameter2)
					first_param = op_codes[op_codes[index+1]] if parameter1 == 0 else op_codes[index+1]
					sec_param = op_codes[op_codes[index+2]] if parameter2 == 0 else op_codes[index+2]
					# print("code 7", first_param, sec_param)
					pos = op_codes[index+3]
					if first_param < sec_param:
						op_codes[pos] = 1
					else:
						op_codes[pos] = 0
					# print("code 7 saving to", pos, op_codes[pos])
					index = index + 4	
				elif actual_opcode == 8:
					# print("code 8", parameter1, parameter2)
					first_param = op_codes[op_codes[index+1]] if parameter1 == 0 else op_codes[index+1]
					sec_param = op_codes[op_codes[index+2]] if parameter2 == 0 else op_codes[index+2]
					# print("code 8", first_param, sec_param)
					pos = op_codes[index+3]
					if first_param == sec_param:
						op_codes[pos] = 1
					else:
						op_codes[pos] = 0
					# print("code 8 saving to", pos, op_codes[pos])
					index = index + 4	
		else:
			if op_codes[index] == 99:
				# print("We're done", op_codes)
				return input_value
			else:
				print("Unknown op code", op_code, "at index", index)
				return op_codes


example1 = [3,9,8,9,10,9,4,9,99,-1,8]
example2 = [3,9,7,9,10,9,4,9,99,-1,8]
example3 = [3,3,1108,-1,8,3,4,3,99]
example4 = [3,3,1107,-1,8,3,4,3,99]
example5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
example6 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
example7 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

process_opcodes(example7, 0)
process_opcodes(example7, 7)
process_opcodes(example7, 8)
process_opcodes(example7, 9)
process_opcodes(example5, 0)
process_opcodes(example5, 1)

process_opcodes(op_codes, 5)









