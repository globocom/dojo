def validate_count_caracters(expression):
	return len(expression) % 2
	
	
def validate_compare_caracters(character):
	open_char = {
		"(":1, ")": -1,
		"[":1, "]": -1,
		"{":1, "}": -1,
		 }
	compare = [ open_char[char] for char in character ]
	print('compare: ', compare)
	print('soma compare: ', sum(compare))
	return True if not sum(compare) else False
	