def check_sort(array):
	for index, element in enumerate(array):
		if index+1 != len(array):
			if element >= array[index+1]:
				return False
	return True

def remove_element(array, index, length):
	return array.pop(index)
	# if length == 2 and index == 0:
	# 	return [6,3,5]
	# if index == 0 : 
	# 	return [2,6,3,5]
	# return [2,3,5]