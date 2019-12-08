import sys

with open('day08_input.txt') as f:
	pixels = f.readlines()
pixels = pixels[0]

example1 = '123456789012'
layers = {}
counts_per_layer = {}

def populate_layers(pixels, width, height, layers):
	idx = 0
	layer_num = 1
	while(idx < len(pixels)):
		current_layer = ''
		for i in range(0, height):
			end = idx + width
			current_layer = pixels[idx:end]
			if layer_num not in layers:
				layers[layer_num] = current_layer
			else:
				layers[layer_num] = layers[layer_num] + current_layer
			idx = idx + width
		layer_num += 1
	return layers


def validate_image(layers, digit_count, digit0, digit1, digit2):
	count_digit0 = 0
	count_digit1 = 0
	count_digit2 = 0
	
	min_count_digit0 = sys.maxint
	key_min_digit0 = ''

	for key, layer in layers.items():
		# print('layer', layer)
		count_digit1 = layer.count(str(digit1))
		count_digit2 = layer.count(str(digit2))
		count_digit0 = layer.count(str(digit0))

		if count_digit0 < min_count_digit0:
			min_count_digit0 = count_digit0
			key_min_digit0 = key

		if key not in digit_count:
			digit_count[key] = {}

		digit_count[key][str(digit1)] = count_digit1
		digit_count[key][str(digit2)] = count_digit2

	return digit_count[key_min_digit0][str(digit1)] * digit_count[key_min_digit0][str(digit2)]


# print(populate_layers(example1, 3, 2, layers))
populate_layers(pixels, 25, 6, layers)
print(validate_image(layers, counts_per_layer, 0, 1, 2))







