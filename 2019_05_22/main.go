package dojo

func getSmaller(slic []int) int {
	smallest := slic[0]
	for i := 1; i < len(slic); i++ {
		if slic[i] < smallest {
			smallest = slic[i]
		}
	}
	return smallest
}

func subtract(slic []int, small int) []int {
	resp := make([]int, 3)
	for i := 0; i < len(slic); i++ {
		resp[i] = slic[i] - small
	}
	return resp
}
