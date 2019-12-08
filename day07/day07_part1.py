
import intcode_computer as ic
import itertools
import sys

with open('day07_input.txt') as f:
    op_codes = f.readlines()

op_codes = map(int, op_codes[0].split(','))

phase_settings = range(0,5)

phase_combos = list(itertools.permutations(phase_settings, 5))

def calc_output_signal(phase_combo, amp_cont_soft):
	output_signal = 0
	print("Current phase combo", phase_combo)
	for i, phase_setting in enumerate(phase_combo):
		if i == 0:
			output_signal = ic.process_opcodes(amp_cont_soft, phase_setting, 0)
		else:
			output_signal = ic.process_opcodes(amp_cont_soft, phase_setting, output_signal)
	print("output_signal", output_signal)
	return output_signal


def calc_max_output_signal(phase_combos, amp_cont_soft):
	max_output_signal = -sys.maxint
	for p in phase_combos:
		curr_output_signal = calc_output_signal(p, amp_cont_soft)
		if curr_output_signal > max_output_signal:
			max_output_signal = curr_output_signal
	return max_output_signal


example1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
example2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]
example3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

print(calc_max_output_signal(phase_combos, op_codes))
