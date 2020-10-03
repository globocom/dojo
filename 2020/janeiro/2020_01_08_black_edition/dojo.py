def brainfuck(instructions):
	vector = [chr(0)] * 30000
	stdout = ""
	pos = 0
	for text in instructions:
		if text == "+":
			vector[pos] = chr(ord(vector[pos])+1)
		elif text == "-":
			vector[pos] = chr(ord(vector[pos])-1)
		elif text == ".":
			stdout += vector[pos]
		elif text == ">":
			pos += 1
		elif text == "<":
			pos -= 1
	return "".join(stdout)