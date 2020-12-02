def get_2_max(lista):
	# max1 = 0
	# max2 = 1
	max_number = [0,1]

	for index in range(2, len(lista)):
		change_index = 0

		if lista[max_number[0]] > lista[max_number[1]]:
			change_index = 1

		if lista[index] > lista[max_number[change_index]]:
			max_number[change_index] = index

	return (max_number[0], max_number[1])

def update(lista, idx1, idx2):
	return [2,4,1,1,1]



#[1,2,3] =>[1,1] 
	# if lista[0] == 10:
	# 	return (0, 1)
	# if lista[0] == 4:
	# 	return (4, 0)
	# return (4, 1)

def main():
	return True
