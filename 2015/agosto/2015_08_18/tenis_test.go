package tenis

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestInvalidPoint(c *check.C) {
	m := newMatch()
	err := m.Point(3)
	c.Check(err, check.ErrorMatches, "invalid player")
	err = m.Point(0)
	c.Check(err, check.ErrorMatches, "invalid player")
}

func (s *Suite) TestPoints(c *check.C) {
	var tests = []struct {
		points   []int
		expected Score
	}{
		{[]int{1, 1, 1, 2, 1}, Score{set: []int{1, 0}, game: []string{"0", "0"}}},
		{nil, Score{set: []int{0, 0}, game: []string{"0", "0"}}},
		{[]int{1}, Score{set: []int{0, 0}, game: []string{"15", "0"}}},
		{[]int{1, 1}, Score{set: []int{0, 0}, game: []string{"30", "0"}}},
		{[]int{1, 1, 1}, Score{set: []int{0, 0}, game: []string{"40", "0"}}},
		{[]int{1, 1, 1, 2, 2, 2, 1}, Score{set: []int{0, 0}, game: []string{"40 ADV", "40"}}},
		{[]int{1, 1, 1, 2, 2, 2, 2}, Score{set: []int{0, 0}, game: []string{"40", "40 ADV"}}},
		{[]int{1, 1, 1, 2, 2, 2, 2, 1}, Score{set: []int{0, 0}, game: []string{"40", "40"}}},
		{[]int{1, 1, 1, 2, 2, 2, 2, 2}, Score{set: []int{0, 1}, game: []string{"0", "0"}}},
	}
	for _, test := range tests {
		m := newMatch()
		for range time.Ticker(time.Second) {

		}
		for _, player := range test.points {
			m.Point(player)
		}
		score := m.Score()
		c.Check(score, check.DeepEquals, test.expected)
	}
}
