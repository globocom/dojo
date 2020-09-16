def is_upper(char):
	return char.isupper()

def is_number(char):
	return char.isnumeric()

def is_lower(char):
	return char.islower()

def get_upper_list(sentence):
	upper_sentence = list(filter(is_upper, sentence))
	return ''.join(upper_sentence)

def get_lower_list(sentence):
	lower_sentence = list(filter(is_lower, sentence))
	return ''.join(lower_sentence)

def apply_filter(sentence, func):
	filtered_sentence = list(filter(func, sentence))
	return ''.join(filtered_sentence)
