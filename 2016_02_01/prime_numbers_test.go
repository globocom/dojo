package prime_numbers

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestSimplePrimeNumbers(c *check.C) {
	cases := map[int]Primes{
		3: Primes{2, 3},
		5: Primes{2, 3, 5},
		20: Primes{2, 3, 5, 7, 11, 13, 17, 19},
		120: Primes{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113},
	}
	for maxValue, expected := range cases {
		c.Check(CalculatePrimes(maxValue), check.DeepEquals, expected)
	}
}

func (s *Suite) TestRemoveItem(c *check.C) {
	list := Primes{1,2,3,4}
	expected := Primes{1,3,4}
	list.RemoveItem(2)
	c.Assert(list, check.DeepEquals, expected)
}
