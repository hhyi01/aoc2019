
import operator
import collections


opcodes = {
	1: operator.add,
	2: operator.mul,
}


def process_opcodes(op_codes, index, *args):
	test_result = 0
	input_values = collections.deque(args)
	print("Input values", input_values)
	while(index < len(op_codes)):
		op_code = op_codes[index]
		print("current op code", op_code, "index", index)
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
			input_value = input_values.popleft()
			print("current input value", input_value)
			op_codes[parameter] = input_value
			index = index + 2
		elif op_code == 4:
			parameter = op_codes[index+1]
			print("Test result 1", op_codes[parameter], "using value", input_value)
			print("current state", test_result, index, op_codes)
			test_result = op_codes[parameter]
			index = index + 2
			return test_result, index, op_codes
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
						print("Test result 2", opcodes[parameter], "using value", input_value)
						test_result = opcodes[parameter]
						print("current state", test_result, index, op_codes)
						return test_result, index, op_codes
					else:
						print("Test result 3", parameter, "using value", input_value)
						test_result = parameter
						print("current state", test_result, index, op_codes)
						return test_result, index, op_codes
					index = index + 2
				elif actual_opcode == 3:
					parameter = op_codes[index+1]
					input_value = input_values.popleft()
					print("current input value", input_value)
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
			if op_code == 99:
				print("We're done 4")
				print("current state", test_result, index, op_codes)
				return test_result, index, op_codes
			else:
				print("Unknown op code", op_code, "at index", index)
				return op_codes







