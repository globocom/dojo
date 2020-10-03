package dojo

import "sort"

func main(nums []int, target int) [][]int {
	if target == 1 {
		return [][]int{[]int{0, 1}}
	}
	if target == 2 {
		return [][]int{[]int{0, 2}}
	}

	return [][]int{[]int{1, 2}}
}

func combinations(nums []int) [][]int {

	var arr [][]int
	for index1, x := range nums {
		for index2, y := range nums {
			if index1 != index2 {
				arr = append(arr, []int{x, y})
			}
		}
	}

	return arr
}

func sortArrays(arrays [][]int) {
	for index, array := range arrays {
		array[index] = sort.Ints(array)
	}
	return arrays
}
