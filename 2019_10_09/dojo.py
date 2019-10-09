def swap_numbers(pos1,pos2,array):
	if pos1 < 0 or pos2 < 0:
		return array
	
	if pos1 >= len(array) or pos2 >= len(array):
		return array
	
	array[pos1], array[pos2] = array[pos2], array[pos1]
	
	return array

def index_less_element(arr):
	return arr.index(min(arr))

def sort_array(arr):
	count = 0
	for x in range(0,len(arr)):
		minValue = index_less_element(arr[x:])
		if minValue is not 0:
			count += 1	
			swap_numbers(x, minValue + x, arr )
		x = x + 1
	return count
