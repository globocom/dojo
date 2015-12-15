package statistics

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestMaxMinValue(c *check.C) {
	values := []int{1, 4, 6, 2, 4, 9, 0}
	statistics := GetStatistics(values)
	c.Assert(statistics.Max, check.Equals, 9)
	c.Assert(statistics.Min, check.Equals, 0)
}

func (s *Suite) TestElementsInSequence(c *check.C) {
	values := []int{1, 4, 6, 2, 4, 9, 0}
	statistics := GetStatistics(values)
	c.Assert(statistics.NumElements, check.Equals, 7)
}

func (s *Suite) TestMean(c *check.C) {
	values := []int{20, 30, 40, 50}
	statistics := GetStatistics(values)
	c.Assert(statistics.Mean, check.Equals, 35)
}
