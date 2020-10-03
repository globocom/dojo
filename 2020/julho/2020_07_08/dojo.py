def string_to_array(letters):
	return list(letters)

def main (jewels, stones):
	jewels_result = string_to_array(jewels)
	return sum([stones.count(jewel) for jewel in jewels_result])