package main

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestP_1_1(c *check.C) {
	c.Assert(P(1, 1), check.Equals, 1) // 1
}

func (s *Suite) TestP_1_2(c *check.C) {
	c.Assert(P(1, 2), check.Equals, 3) // 3
}

func (s *Suite) TestP_1_3(c *check.C) {
	c.Assert(P(1, 3), check.Equals, 6) // 6
}

func (s *Suite) TestP_1_4(c *check.C) {
	c.Assert(P(1, 4), check.Equals, 10) // 10
}

func (s *Suite) TestP_1_5(c *check.C) {
	c.Assert(P(1, 5), check.Equals, 15) // 15
}

func (s *Suite) TestP_1_6(c *check.C) {
	c.Assert(P(1, 6), check.Equals, 21) // 21
}

func (s *Suite) TestP_2_1(c *check.C) {
	c.Assert(P(2, 1), check.Equals, 2)
}

func (s *Suite) TestP_2_2(c *check.C) {
	c.Assert(P(2, 2), check.Equals, 7)
}

func (s *Suite) TestP_2_3(c *check.C) {
	c.Assert(P(2, 3), check.Equals, 9)
}

func (s *Suite) TestP_2_4(c *check.C) {
	c.Assert(P(2, 4), check.Equals, 16)
}

func (s *Suite) TestP_3_1(c *check.C) {
	c.Assert(P(3, 1), check.Equals, 4)
}

func (s *Suite) TestP_3_2(c *check.C) {
	c.Assert(P(3, 2), check.Equals, 5)
}

func (s *Suite) TestP_3_3(c *check.C) {
	c.Assert(P(3, 3), check.Equals, 11)
}

func (s *Suite) TestP_3_4(c *check.C) {
	c.Assert(P(3, 4), check.Equals, 14)
}

func (s *Suite) TestP_4_1(c *check.C) {
	c.Assert(P(4, 1), check.Equals, 8)
}

func (s *Suite) TestP_4_2(c *check.C) {
	c.Assert(P(4, 2), check.Equals, 17)
}

func (s *Suite) TestP_4_3(c *check.C) {
	c.Assert(P(4, 3), check.Equals, 19)
}

func (s *Suite) TestP_4_4(c *check.C) {
	c.Assert(P(4, 4), check.Equals, 30)
}

func (s *Suite) TestP_5_5(c *check.C) {
	c.Assert(P(5, 5), check.Equals, 38)
}

func (s *Suite) TestP_10_1(c *check.C) {
	c.Assert(P(10, 1), check.Equals, 50)
}

func (s *Suite) TestP_10_20(c *check.C) {
	c.Assert(P(10, 20), check.Equals, 440)
}

func (s *Suite) TestP_25_75(c *check.C) {
	c.Assert(P(25, 75), check.Equals, 4863)
}

func (s *Suite) TestP_99_100(c *check.C) {
	c.Assert(P(99, 100), check.Equals, 19454)
}

func (s *Suite) TestSum(c *check.C) {
	c.Assert(S(71328803586048), check.Equals, 40632119)
}
