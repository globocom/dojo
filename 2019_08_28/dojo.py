def count_vowels(word):
	count = 0
	for letter in word:
		if letter in ['a','e','i','o','u']:
			count += 1
	return count


def get_score(word):
	if (count_vowels(word)%2) == 0:
		return 2
	return 1

def get_total_score(sentence):
	words = sentence.split(" ")
	count = 0 
	for word in words:
		count += get_score(word)
	return count