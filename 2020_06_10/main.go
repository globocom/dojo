package dojo

func main(array []int, index int) int {
	minValue := index
	for i := index + 1; i < len(array); i++ {
		if array[minValue] > array[i] {
			minValue = i
		}
	}
	return minValue
}
