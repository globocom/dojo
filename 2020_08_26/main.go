package dojo

func combineArrays(firstArray, secondArray []int) [][]int {
	combinedMatriz := [][]int{}

	for _, v := range firstArray {
		for _, v2 := range secondArray {
			combinedMatriz = append(combinedMatriz, []int{v, v2})
		}
	}
	return combinedMatriz
}

func sortElements(primaryArray [][]int) [][]int {
	auxMatriz := [][]int{}
	for i, v1 := range primaryArray {
		for j, v2 := range v1 {
			map[int]int 
		}
	}
	// if len(primaryArray) == 4 {
	// 	return [][]int{{1, 2}, {2, 3}, {3, 2}, {3, 3}}
	// }
	// if len(primaryArray) == 6 {
	// 	return [][]int{{1, 2}, {1, 3}, {2, 2}, {2, 3}, {3, 2}, {3, 3}}
	// }
	// return [][]int{{1, 2}, {1, 3}}
}

// Ingrid - Beza - Sami - Juan - Elen - Allan - Natalia
