package dojo

func rotate(arr [3]int) [3]int {
	auxArr := arr[0]
	arr[0] = arr[1]
	arr[1] = arr[2]
	arr[2] = auxArr

	return arr
}

func isOrdered(arr [3]int, index int) bool {
	return arr[index] == (index + 1)
}
