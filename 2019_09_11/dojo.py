def min_array_slices(arr, index):
	arr1 = arr[:index]
	arr2 = arr[index:]

	return [sum(arr1),sum(arr2)]

def min_iterate(arr):
	result = None
	for key, value in enumerate(arr):
		r = min_array_slices(arr, key)
		r = r[1] - r[0]
		if not result or r < result:
			result = r
	
	return abs(result)

def array_shuffle(arr):
	is_even = len(arr) % 2 == 0
	if is_even:
		while len(arr) > (len(arr)/2):
	# if len(arr) == 4: 
	# 	return [1,4,2,3]
	# if len(arr)==3:
	# 	return [1,2,3]
	# return [2,1]