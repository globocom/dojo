package main

import (
  "testing"
  "gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(Suite{})

type Suite struct{}

func (Suite) TestIsNotPalyndrome(c *check.C) {
	c.Assert(IsPalyndrome(123), check.Equals, false)
}

func (Suite) TestIsPalyndrome(c *check.C) {
	c.Assert(IsPalyndrome(1001), check.Equals, true)
}

func (Suite) TestCalcLargestPalyndromeWith2Digits(c *check.C) {
	c.Assert(CalcLargestPalyndrome(2), check.Equals, 9009)
}

func (Suite) TestCalcLargestPalyndromeWith3Digits(c *check.C) {
	c.Assert(CalcLargestPalyndrome(3), check.Equals, 906609)
}
