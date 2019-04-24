package dojo

func shiftPos(arr [5]int, position int) [5]int {
	expected := arr

	expected[position+1] = expected[position]

	return expected
}

func lockupPos(arr [5]int) int {
	lastPosition := len(arr) - 1
	for i := range arr {
		if arr[i] > arr[lastPosition] {
			return i
		}
	}
	return -1
}

func main(arr [5]int) [][5]int {
	result := [][5]int{}
	first := shiftPos(arr, 3)
	result = append(result, first)
	pos := lockupPos(arr)
	interations := (len(arr) - 1) - pos

	for i := len(arr) - 2; i <= interations; i-- {
		newArr := shiftPos(arr, i)
		result = append(result, newArr)
	}
	return result
	// 	expected := [][5]int{
	// 		[5]int{2, 4, 6, 8, 7},
	// 		[5]int{2, 4, 6, 8, 8},
	// 		[5]int{2, 4, 6, 7, 8},
	// 	}
	// 	return expected
}
