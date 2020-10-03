package prime_numbers

import "math"

type Primes []int

func (p *Primes) RemoveItem(item int) {
	var newPrimeList Primes
	for _,v := range (*p) {
		if (v != item) {
			newPrimeList = append(newPrimeList, v)
		}
	}
	*p = newPrimeList
}

func CreateList(maxValue int) Primes {
	var values Primes
	for i := 2; i <= maxValue; i++ {
		values = append(values, i)
	}
	return values
}

func CalculatePrimes(maxValue int) Primes {
	maxIterating := int(math.Sqrt(float64(maxValue)))
	values := CreateList(maxValue)
	for i := 2; i <= maxIterating; i++ {
		for _,v := range values {
			if (v != i && v % i == 0) {
				values.RemoveItem(v)
			}
		}
	}
	return values
}
