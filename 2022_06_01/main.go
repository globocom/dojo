package dojo
import (
	"fmt"
	"strings"
	"strconv"
)

func main() bool {
	return true
}

func calculateChecksum(input string) int {
	lines := [][]int{}
	for _,line := range strings.Split(input, "\n") {
		lines = append(lines, ParseLine(line))
	}

	checksum := 0
	for _,line := range lines {
		checksum += GetLineChecksum(ExtractMinMaxNumber(line))
	}
	
	return checksum
}

func ParseLine(line string) (output []int) {
	for _, numberStr := range strings.Split(line, "\t") {
		numberInt, err := strconv.Atoi(numberStr)
		if err != nil {
			fmt.Println(err)
		}
		output = append(output, numberInt)
	}
	return
}

func ExtractMinMaxNumber(line []int) (int, int) {
	min := line[0]
	max := line[0]
	for _, element := range line {
		if element < min {
			min = element
		}
		if element > max {
			max = element
		}
	}
	return min, max
}

func GetLineChecksum(min int, max int) int {
	return max - min
}


func calculateChecksumPartTwo(input string) int {
	lines := [][]int{}
	for _,line := range strings.Split(input, "\n") {
		lines = append(lines, ParseLine(line))
	}

	checksum := 0
	for _,line := range lines {
		checksum += findDivisibleLine(line)
	}
	
	return checksum
}

func findDivisibleLine(line []int) int {
	for index, element := range line {
		for innerIndex, innerElement := range line {
			if index == innerIndex {
				continue
			}

			if (element % innerElement) == 0 {
				return element / innerElement
			}
		}
	}
	return 0
}

//
// 1 - receber input
// 2 - ler linha a linha do input
// 2.1 - ler cada numero separado por \t
	// e colocar em uma lista
	// convertendo para numerico
// 2.2 - percorrer a lista e achar 
	// o maior e menor numero
// 2.3 - calcular a diferença entre eles
// 3 - somar todas as diferenças
//

// Pedro
// Victor
// Raphael 
// Paulo
// Carreira
