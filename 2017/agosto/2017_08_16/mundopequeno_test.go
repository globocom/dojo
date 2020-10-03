package main

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

type DojoSuite struct {
	person *person
}

var _ = check.Suite(&DojoSuite{})

func (s *DojoSuite) SetUpSuite(c *check.C) {
	s.person = &person{
		x: 1.0,
		y: 1.0,
	}
}

func (s *DojoSuite) TestCoordinates(c *check.C) {
	c.Assert(s.person.x, check.Equals, 1.0)
	c.Assert(s.person.y, check.Equals, 1.0)
}

func (s *DojoSuite) TestDistanceTwoPeople(c *check.C) {
	people := []person{
		person{x: 3.0, y: 0.0},
		person{x: 0.0, y: 4.0},
	}
	c.Assert(distance(people[0], people[1]), check.DeepEquals, 5.0)
}

func (s *DojoSuite) TestCloser(c *check.C) {
	people := []person{
		person{x: 1.2, y: 1.2},
		person{x: 5.0, y: 4.0},
	}
	c.Assert(s.person.closer(people)[0], check.DeepEquals, people[0])
}

func (s *DojoSuite) TestCloserTwo(c *check.C) {
	people := []person{
		person{x: 5.0, y: 4.0},
		person{x: 1.2, y: 1.2},
	}
	c.Assert(s.person.closer(people)[0], check.DeepEquals, people[1])
}
