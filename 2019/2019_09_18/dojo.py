def main(matrix):
	result = ""
	for i in range(0, len(matrix[0])):
		for k in range(0, len(matrix)):
			char = matrix[k][i]
			if len(result) > 0 and result[-1] == "!" and char != "!":
				result = result[:-1] + " "
			result += char

	return result

def parser_string(string):	
	# if string[:-1]== "!":
	# 	return string.replace("!", " ")
	return string.replace("!", " ")
	# if string == 'olavey':
	# 	return 'olavey'
	# if string == 'olavey!':
	# 	return 'olavey!'
	# return 'ola ey'