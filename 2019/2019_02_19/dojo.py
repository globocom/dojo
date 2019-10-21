def in_array(arrayNumber,valor):
	return valor in arrayNumber

def array_list(matriz):
	arr = []
	if len(matriz) == 2:
		for item in matriz[0]:
			if in_array(matriz[1], item):
				arr.append(item)
		return arr
	
	if matriz[0][0]== 0:
		return []
	return [1]
	# for item in matriz[0]:
	# 	if in_array(matriz[1], item) and in_array(matriz[2], item):
	# 		arr.append(item)
	# return arr
