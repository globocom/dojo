def get_dependencies(wall, target):
	response = set()
	for i in range(len(wall) - 1):
		for j in range(len(wall[i])):
			if ((wall[i][j] != wall[i+1][j]) and (wall[i][j] == target)):
				response.add(wall[i+1][j])
	if len(response) == 0:
		return None
	return response

def remove_repeted_letters(wall):
	result = set()
	for line in wall:
		result = result | set(line)
	return result

def get_dict_dependencies(wall):

	letters = remove_repeted_letters(wall)
	result_letter = {}

	for letter in letters:
		result_letter[letter]=get_dependencies(wall, letter)

	return result_letter

# For passando pelas letras e chamando o get_dependencies p/ pegar as dependencias das letras

# Ordena
# a: {'b'}, b: {'c'}, c: {'e', 'd'}, d:{'e', 'a'}, e:None
# ['E']