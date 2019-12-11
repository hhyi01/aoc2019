import intcode_computer as ic

with open('day09_input.txt') as f:
    op_codes = f.readlines()

op_codes = map(int, op_codes[0].split(','))
# print(op_codes)


def get_boost_keycode(op_codes, input_value):
	return ic.process_opcodes(op_codes, input_value)


example1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
example2 = [1102,34915192,34915192,7,4,7,99,0]
example3 = [104,1125899906842624,99]
print(get_boost_keycode(op_codes, 1))


