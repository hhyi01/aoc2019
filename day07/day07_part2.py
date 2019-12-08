
import intcode_computer as ic
import itertools
import sys

with open('day07_input.txt') as f:
    op_codes = f.readlines()

op_codes = map(int, op_codes[0].split(','))

phase_settings = range(5,10)

phase_combos = list(itertools.permutations(phase_settings, 5))

amp_states = {}

def calc_output_signal(phase_combo, amp_cont_soft, output_signal, index):
	print("Current phase combo", phase_combo)
	for i, phase_setting in enumerate(phase_combo):
		print("Amplifier", i)
		if i not in amp_states:
			amp_states[i] = {}
			if i > 0:
				output_signal = amp_states[i-1]['output_signal']
			amp_states[i]['output_signal'], amp_states[i]['instruction_pt'], amp_states[i]['op_codes'] = \
				ic.process_opcodes(amp_cont_soft, index, phase_setting, output_signal)
		else:
			if i == 0:
				amp_states[i]['output_signal'], amp_states[i]['instruction_pt'], amp_states[i]['op_codes'] =  \
					ic.process_opcodes(amp_states[i]['op_codes'], amp_states[i]['instruction_pt'], phase_setting, amp_states[len(phase_combo)-1]['output_signal'])
			else:
				amp_states[i]['output_signal'], amp_states[i]['instruction_pt'], amp_states[i]['op_codes'] =  \
					ic.process_opcodes(amp_states[i]['op_codes'], amp_states[i]['instruction_pt'], phase_setting, amp_states[i-1]['output_signal'])
	return amp_states[len(phase_combo)-1]['output_signal']


def calc_max_output_signal(phase_combos, amp_cont_soft):
	max_output_signal = -sys.maxint
	for p in phase_combos:
		curr_output_signal = calc_output_signal(p, amp_cont_soft)
		if curr_output_signal > max_output_signal:
			max_output_signal = curr_output_signal
	return max_output_signal


def set_feedback_loop(phase_combo, amp_cont_soft):
	loop = 0
	curr_output_signal = 0
	while(loop < 5):
		if loop == 0:
			curr_output_signal = calc_output_signal(phase_combo, amp_cont_soft, 0, 0)
		else:
			curr_output_signal = calc_output_signal(phase_combo, amp_cont_soft, curr_output_signal, 0)
		loop += 1
		print("output_signal", curr_output_signal, "at loop", loop)
	return curr_output_signal


example1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
example2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

# print(calc_output_signal([9,8,7,6,5], example1, 0, 0))
print(set_feedback_loop([9,8,7,6,5], example1))
