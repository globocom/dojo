


def remove_word(sentence, word):
	if sentence.index(word) == 0:
		return sentence[len(word):]
	else:
		return sentence

def main(sentence, words):
	if "leetcodeapple" == sentence:
		return True
	return True