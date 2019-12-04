
puzzle_input_start = 153517
puzzle_input_end = 630395

# validation steps

# should be 6 digit number
def verify_number_length(num):
	return len(str(num)) == 6

# should be within input range
def verify_within_range(num, start, end):
	return num >= start and num <= end

# should have 2 adjacent digits that are equal
def verify_two_adj_digits(num):
	has_same_two_adj_digits = False
	for i in range(1, len(str(num))):
		prev_digit = str(num)[i-1]
		curr_digit = str(num)[i]
		if prev_digit == curr_digit:
			has_same_two_adj_digits = True
			break
	return has_same_two_adj_digits

# should have non-decreasing digits from left to right
def verify_non_decreasing(num):
	is_non_decreasing = True
	for i in range(1, len(str(num))):
		prev_digit = str(num)[i-1]
		curr_digit = str(num)[i]
		if curr_digit < prev_digit:
			is_non_decreasing = False
			break
	return is_non_decreasing

def count_passwords_within_range(start, end):
	num_passwords = 0
	for num in range(start, end+1):
		if verify_number_length(num):
			if verify_two_adj_digits(num):
				if verify_non_decreasing(num):
					num_passwords += 1
	return num_passwords


print(verify_non_decreasing(123789)) # should be True
print(verify_two_adj_digits(123789)) # should be False

print(count_passwords_within_range(puzzle_input_start, puzzle_input_end))
