import sys

with open('day08_input.txt') as f:
	pixels = f.readlines()
pixels = pixels[0]

example1 = '0222112222120000'
layers = {}
counts_per_layer = {}

def populate_layers(pixels, width, height, layers):
	idx = 0
	layer_num = 1
	while(idx < len(pixels)):
		current_layer = ''
		line = 0
		for i in range(0, height):
			end = idx + width
			current_layer = pixels[idx:end]
			if layer_num not in layers:
				layers[layer_num] = {}
				layers[layer_num][line] = current_layer
			else:
				layers[layer_num][line] = current_layer
			line += 1
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


def render_image(layers, width, height):
	black = '0'
	white = '1'
	transparent = '2'
	image = [[None for i in range(width)] for n in range(height)]

	for x in range(0, height):
		for y in range(0, width):
			rendered_pixel = ''
			for k, layer in layers.items():
				if layer[x][y] == transparent:
					continue
				if layer[x][y] == black:
					# rendered_pixel = rendered_pixel + layer[x][y]
					rendered_pixel = rendered_pixel + ' '
					break
				if layer[x][y] == white:
					rendered_pixel = rendered_pixel + layer[x][y]
					break
			image[x][y] = rendered_pixel

	return image


# populate_layers(example1, 2, 2, layers)
populate_layers(pixels, 25, 6, layers)
image = render_image(layers, 25, 6)

for line in image:
	s = ''
	print(s.join(line))



