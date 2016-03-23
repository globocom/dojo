package main

import (
	"fmt"
	. "math"
	. "math/big"
)

func gimmeTheSum(f, r Int) *Int {
	var sum Int
	sum.Add(&f, &r)
	var m Int
	sum.DivMod(&sum, NewInt(2), &m)
	if m.Cmp(NewInt(0)) == 0 { // check if f+r is even
		return NewInt(1)
	}
	return NewInt(-1)
}

func P(f, r *Int) *Int {
	sum := NewInt(0)
	if f.Cmp(NewInt(1)) == 0 {
		sum.Add(r, NewInt(1))
		sum.Mul(sum, r)
		sum.Div(sum, NewInt(2))
	} else {
		// return P(1, f+r-1-(f%2)) + gimmeTheSum(f, r)*(f/2)
		sum.Add(sum, f)
		sum.Add(sum, r)
		sum.Sub(sum, NewInt(1))
		var mod Int
		q := NewInt(0)
		q.Add(q, f)
		q.DivMod(f, NewInt(2), &mod)
		sum.Sub(sum, &mod)
		p := P(NewInt(1), sum)
		prod := NewInt(0)
		prod.Add(prod, f)
		prod.Div(f, NewInt(2))
		prod.Mul(gimmeTheSum(*f, *r), prod)
		sum.Add(p, prod)
		// return P(1, f+r-1-(f%2)) + gimmeTheSum(f, r)*(f/2)
	}
	return sum
}

func S(m int64) string {
	var sum Int
	sqrt := NewInt(int64(Sqrt(float64(m))))
	for f := NewInt(1); f.Cmp(sqrt) < 0; f.Add(f, NewInt(1)) {
		x := NewInt(m)
		x.Mod(x, f)
		if x.Cmp(NewInt(0)) == 0 {
			bigM := NewInt(m)
			r := bigM.Div(bigM, f)
			// r := m / f
			sum.Add(&sum, P(f, r))
			sum.Add(&sum, P(r, f))
			// sum += P(f, r) + P(r, f)
		}
	}
	str := sum.String()
	return str[len(str)-8 : len(str)]
}

func main() {
	fmt.Println(S(71328803586048))
}
