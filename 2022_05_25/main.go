package dojo

import (
	"strconv"
)

func main() bool {
	return true;
}

func process_day1(input string) int {
	sum := 0
	last_number := string(input[len(input)-1])

	for _, v := range input {
		c := string(v)
		if c == last_number {
			if number, err := strconv.Atoi(c) ; err == nil {
				sum += number
			}
		}
		last_number = c
	}
	return sum
}


func process_day2(input string) int {
	sum := 0
	midIdx := len(input)/2

	for _, v := range input {
		c := string(v)
		lastNumber := string(input[midIdx])
		if c == lastNumber {
			if number, err := strconv.Atoi(c) ; err == nil {
				sum += number
			}
		}
		midIdx = (midIdx + 1) % len(input)
	}
	return sum
}


// 1 - função que lerá a expressão e retornará um número inteiro
// 2 - ler cada caracter comparando com o seu vizinho proximo
// 2.1 - soma o digito valido quando o proprio for igual ao proximo em uma variavel auxiliar
//


// Pedro
// Kairo
// Raphael
// Carreira
// Fernando
// Brendo
