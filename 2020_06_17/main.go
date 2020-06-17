package dojo

import "math"

// recebe inteiro
func convertBitPos(pos int, bit int) int {
	// converte pra float
	posFloat := float64(pos)
	bitFloat := float64(bit)
	return int(bitFloat * math.Pow(2, posFloat))
}

func main(numbers []int) int {
	soma := 0
	currentPos := 0
	for i := len(numbers) - 1; i >= 0; i-- {
		soma += convertBitPos(currentPos, numbers[i])
		currentPos++
	}
	return soma
}
