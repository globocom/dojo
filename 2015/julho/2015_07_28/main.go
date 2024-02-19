package main

import (
  "fmt"
  "strconv"
  "math"
)

func main() {
  fmt.Println(CalcLargestPalyndrome(3))
}

func CalcLargestPalyndrome(numDigits int) int {
  start := int(math.Pow10(numDigits - 1))
  end := int(math.Pow10(numDigits) - 1)
  largestPalyndrome := 0

  for i := start;  i <= end; i++ {
    for j := i;  j <= end; j++ {
      num := i * j
      if IsPalyndrome(num) && num > largestPalyndrome {
        largestPalyndrome = num
      }

    }
  }

  return largestPalyndrome
}

func IsPalyndrome(number int) bool {
  numberString := strconv.Itoa(number)
  oldString := numberString
  newString := Reverse(numberString)

  return newString == oldString
}

func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}
