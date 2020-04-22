package dojo

func diagonalSoma(matriz [][]int) int {
	var length int = len(matriz[0])
	sum := 0

	for i := 0; i < length; i++ {
		sum = sum + matriz[i][i]
	}
	return sum
}

func diagonalSomaSecond(matriz [][]int) int {
	var length int = len(matriz[0])
	sum := 0

	for i := 0; i < length; i++ {
		sum = sum + matriz[i][length-i-1]
	}
	return sum
}

// func main(matriz [][]int) int {

// }
