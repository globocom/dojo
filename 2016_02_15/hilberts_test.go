package main

import (
	"fmt"
	. "math/big"
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestP_1_r(c *check.C) {
	c.Check((P(1, 1)).Cmp(NewInt(1)), check.Equals, 0)
	c.Check((P(1, 2)).Cmp(NewInt(3)), check.Equals, 0)
	c.Check((P(1, 3)).Cmp(NewInt(6)), check.Equals, 0)
	c.Check((P(1, 4)).Cmp(NewInt(10)), check.Equals, 0)
	c.Check((P(1, 5)).Cmp(NewInt(15)), check.Equals, 0)
	c.Check((P(1, 6)).Cmp(NewInt(21)), check.Equals, 0)
	c.Check((P(1, 7)).Cmp(NewInt(28)), check.Equals, 0)
	c.Check((P(1, 8)).Cmp(NewInt(36)), check.Equals, 0)
	c.Check((P(1, 9)).Cmp(NewInt(45)), check.Equals, 0)
	c.Check((P(1, 10)).Cmp(NewInt(55)), check.Equals, 0)
}

func (s *Suite) TestP_2_r(c *check.C) {
	c.Check((P(2, 1)).Cmp(NewInt(2)), check.Equals, 0)
	c.Check((P(2, 2)).Cmp(NewInt(7)), check.Equals, 0)
	c.Check((P(2, 3)).Cmp(NewInt(9)), check.Equals, 0)
	c.Check((P(2, 4)).Cmp(NewInt(16)), check.Equals, 0)
	c.Check((P(2, 5)).Cmp(NewInt(20)), check.Equals, 0)
	c.Check((P(2, 6)).Cmp(NewInt(29)), check.Equals, 0)
	c.Check((P(2, 7)).Cmp(NewInt(35)), check.Equals, 0)
	c.Check((P(2, 8)).Cmp(NewInt(46)), check.Equals, 0)
	c.Check((P(2, 9)).Cmp(NewInt(54)), check.Equals, 0)
	c.Check((P(2, 10)).Cmp(NewInt(67)), check.Equals, 0)
}

func (s *Suite) TestP_3_r(c *check.C) {
	c.Check((P(3, 1)).Cmp(NewInt(4)), check.Equals, 0)
	c.Check((P(3, 2)).Cmp(NewInt(5)), check.Equals, 0)
	c.Check((P(3, 3)).Cmp(NewInt(11)), check.Equals, 0)
	c.Check((P(3, 4)).Cmp(NewInt(14)), check.Equals, 0)
	c.Check((P(3, 5)).Cmp(NewInt(22)), check.Equals, 0)
	c.Check((P(3, 6)).Cmp(NewInt(27)), check.Equals, 0)
	c.Check((P(3, 7)).Cmp(NewInt(37)), check.Equals, 0)
	c.Check((P(3, 8)).Cmp(NewInt(44)), check.Equals, 0)
	c.Check((P(3, 9)).Cmp(NewInt(56)), check.Equals, 0)
	c.Check((P(3, 10)).Cmp(NewInt(65)), check.Equals, 0)
}

func (s *Suite) TestP_4_r(c *check.C) {
	c.Check((P(4, 1)).Cmp(NewInt(8)), check.Equals, 0)
	c.Check((P(4, 2)).Cmp(NewInt(17)), check.Equals, 0)
	c.Check((P(4, 3)).Cmp(NewInt(19)), check.Equals, 0)
	c.Check((P(4, 4)).Cmp(NewInt(30)), check.Equals, 0)
	c.Check((P(4, 5)).Cmp(NewInt(34)), check.Equals, 0)
	c.Check((P(4, 6)).Cmp(NewInt(47)), check.Equals, 0)
	c.Check((P(4, 7)).Cmp(NewInt(53)), check.Equals, 0)
	c.Check((P(4, 8)).Cmp(NewInt(68)), check.Equals, 0)
	c.Check((P(4, 9)).Cmp(NewInt(76)), check.Equals, 0)
	c.Check((P(4, 10)).Cmp(NewInt(93)), check.Equals, 0)
}

func (s *Suite) TestP_5_r(c *check.C) {
	c.Check((P(5, 1)).Cmp(NewInt(12)), check.Equals, 0)
	c.Check((P(5, 2)).Cmp(NewInt(13)), check.Equals, 0)
	c.Check((P(5, 3)).Cmp(NewInt(23)), check.Equals, 0)
	c.Check((P(5, 4)).Cmp(NewInt(26)), check.Equals, 0)
	c.Check((P(5, 5)).Cmp(NewInt(38)), check.Equals, 0)
	c.Check((P(5, 6)).Cmp(NewInt(43)), check.Equals, 0)
	c.Check((P(5, 7)).Cmp(NewInt(57)), check.Equals, 0)
	c.Check((P(5, 8)).Cmp(NewInt(64)), check.Equals, 0)
	c.Check((P(5, 9)).Cmp(NewInt(80)), check.Equals, 0)
	c.Check((P(5, 10)).Cmp(NewInt(89)), check.Equals, 0)
}

func (s *Suite) TestP_6_r(c *check.C) {
	c.Check((P(6, 1)).Cmp(NewInt(18)), check.Equals, 0)
	c.Check((P(6, 2)).Cmp(NewInt(31)), check.Equals, 0)
	c.Check((P(6, 3)).Cmp(NewInt(33)), check.Equals, 0)
	c.Check((P(6, 4)).Cmp(NewInt(48)), check.Equals, 0)
	c.Check((P(6, 5)).Cmp(NewInt(52)), check.Equals, 0)
	c.Check((P(6, 6)).Cmp(NewInt(69)), check.Equals, 0)
	c.Check((P(6, 7)).Cmp(NewInt(75)), check.Equals, 0)
	c.Check((P(6, 8)).Cmp(NewInt(94)), check.Equals, 0)
	c.Check((P(6, 9)).Cmp(NewInt(102)), check.Equals, 0)
	c.Check((P(6, 10)).Cmp(NewInt(123)), check.Equals, 0)
}

func (s *Suite) TestP_7_r(c *check.C) {
	c.Check((P(7, 1)).Cmp(NewInt(24)), check.Equals, 0)
	c.Check((P(7, 2)).Cmp(NewInt(25)), check.Equals, 0)
	c.Check((P(7, 3)).Cmp(NewInt(39)), check.Equals, 0)
	c.Check((P(7, 4)).Cmp(NewInt(42)), check.Equals, 0)
	c.Check((P(7, 5)).Cmp(NewInt(58)), check.Equals, 0)
	c.Check((P(7, 6)).Cmp(NewInt(63)), check.Equals, 0)
	c.Check((P(7, 7)).Cmp(NewInt(81)), check.Equals, 0)
	c.Check((P(7, 8)).Cmp(NewInt(88)), check.Equals, 0)
	c.Check((P(7, 9)).Cmp(NewInt(108)), check.Equals, 0)
	c.Check((P(7, 10)).Cmp(NewInt(117)), check.Equals, 0)
}

func (s *Suite) TestP_8_r(c *check.C) {
	c.Check((P(8, 1)).Cmp(NewInt(32)), check.Equals, 0)
	c.Check((P(8, 2)).Cmp(NewInt(49)), check.Equals, 0)
	c.Check((P(8, 3)).Cmp(NewInt(51)), check.Equals, 0)
	c.Check((P(8, 4)).Cmp(NewInt(70)), check.Equals, 0)
	c.Check((P(8, 5)).Cmp(NewInt(74)), check.Equals, 0)
	c.Check((P(8, 6)).Cmp(NewInt(95)), check.Equals, 0)
	c.Check((P(8, 7)).Cmp(NewInt(101)), check.Equals, 0)
	c.Check((P(8, 8)).Cmp(NewInt(124)), check.Equals, 0)
	c.Check((P(8, 9)).Cmp(NewInt(132)), check.Equals, 0)
	c.Check((P(8, 10)).Cmp(NewInt(157)), check.Equals, 0)
}

func (s *Suite) TestP_9_r(c *check.C) {
	c.Check((P(9, 1)).Cmp(NewInt(40)), check.Equals, 0)
	c.Check((P(9, 2)).Cmp(NewInt(41)), check.Equals, 0)
	c.Check((P(9, 3)).Cmp(NewInt(59)), check.Equals, 0)
	c.Check((P(9, 4)).Cmp(NewInt(62)), check.Equals, 0)
	c.Check((P(9, 5)).Cmp(NewInt(82)), check.Equals, 0)
	c.Check((P(9, 6)).Cmp(NewInt(87)), check.Equals, 0)
	c.Check((P(9, 7)).Cmp(NewInt(109)), check.Equals, 0)
	c.Check((P(9, 8)).Cmp(NewInt(116)), check.Equals, 0)
	c.Check((P(9, 9)).Cmp(NewInt(140)), check.Equals, 0)
	c.Check((P(9, 10)).Cmp(NewInt(149)), check.Equals, 0)
}

func (s *Suite) TestP_10_r(c *check.C) {
	c.Check((P(10, 1)).Cmp(NewInt(50)), check.Equals, 0)
	c.Check((P(10, 2)).Cmp(NewInt(71)), check.Equals, 0)
	c.Check((P(10, 3)).Cmp(NewInt(73)), check.Equals, 0)
	c.Check((P(10, 4)).Cmp(NewInt(96)), check.Equals, 0)
	c.Check((P(10, 5)).Cmp(NewInt(100)), check.Equals, 0)
	c.Check((P(10, 6)).Cmp(NewInt(125)), check.Equals, 0)
	c.Check((P(10, 7)).Cmp(NewInt(131)), check.Equals, 0)
	c.Check((P(10, 8)).Cmp(NewInt(158)), check.Equals, 0)
	c.Check((P(10, 9)).Cmp(NewInt(166)), check.Equals, 0)
	c.Check((P(10, 10)).Cmp(NewInt(195)), check.Equals, 0)
}

func (s *Suite) TestP_10_20(c *check.C) {
	c.Check((P(10, 20)).Cmp(NewInt(440)), check.Equals, 0)
}

func (s *Suite) TestP_25_75(c *check.C) {
	c.Check((P(25, 75)).Cmp(NewInt(4863)), check.Equals, 0)
}

func (s *Suite) TestP_99_100(c *check.C) {
	c.Check((P(99, 100)).Cmp(NewInt(19454)), check.Equals, 0)
}

func (s *Suite) TestSum(c *check.C) {
	sum := fmt.Sprintf("%d", S(71328803586048))
	c.Check(sum[len(sum)-8:], check.Equals, "40632119")
}
