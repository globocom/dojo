def quantity_letter(word, letter):
	return word.count(letter)

def quantity_letters(word):
	letters_count = {}
	
	for letter in sorted(set(word)):
		letters_count[letter] = quantity_letter(word, letter)
	return letters_count

def main(word):
	quantity_letter_word = quantity_letters(word)
	sorted_letters = {k: v for k, v in sorted(quantity_letter_word.items(), key=lambda item: item[1], reverse=True)}

	answer = {}

	for letter in list(sorted_letters)[:3]:
		answer[letter] = sorted_letters[letter]
	
	return answer
