package main

import (
	"testing"

	check "gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

// 0000 == 10
func (s *Suite) TestNOS_10(c *check.C) {
	result := NOS("0000")
	c.Check(result, check.Equals, 10)
}

func (s *Suite) TestNOS_2(c *check.C) {
	result := NOS("0001")
	c.Check(result, check.Equals, 2)
}

func (s *Suite) TestNOS_10_2(c *check.C) {
	result := NOS("02212")
	c.Check(result, check.Equals, 10)
}

func (s *Suite) TestNOS_21(c *check.C) {
	result := NOS("10020")
	c.Check(result, check.Equals, 21)
}

func (s *Suite) TestReverseNOS(c *check.C) {
	result := SON(10)
	c.Check(result, check.HasLen, 4)
}
