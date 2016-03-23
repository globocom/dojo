package main

import (
	"fmt"
	. "math"
	. "math/big"
)

func gimmeTheSum(f, r int64) int64 {
	if (f+r)%2 == 0 { // check if f+r is even
		return 1
	}
	return -1
}

func P(f, r int64) *Int {
	if f == 1 {
		p := NewInt(r)
		p.Mul(p, NewInt(r+1))
		return p.Div(p, NewInt(2)) // Thanks, Gauss!
	} else {
		p := P(1, f+r-1-(f%2))
		p.Add(p, NewInt((f/2)*gimmeTheSum(f, r)))
		return p
	}
	return nil
}

func S(m int64) *Int {
	sum := NewInt(0)
	sqrtM := int64(Sqrt(float64(m)))
	for f := int64(1); f < sqrtM; f++ {
		if m%f == 0 {
			r := m / f
			s := P(f, r)
			s.Add(s, P(r, f))
			sum.Add(sum, s)
		}
	}
	return sum
}

func main() {
	fmt.Printf("%d", S(71328803586048))
}
