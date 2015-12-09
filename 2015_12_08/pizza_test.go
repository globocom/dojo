package pizza

import (
	"sort"
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestPizza(c *check.C) {
	results := SharePizzaWith("Luca", "Quatro Queijos")
	sort.Strings(results)
	c.Assert(results, check.DeepEquals, []string{"Lenon", "Renata", "Renato", "Tino"})
}

func (s *Suite) TestPizzaNoResult(c *check.C) {
	results := SharePizzaWith("Luca", "Marguerita")
	sort.Strings(results)
	c.Assert(results, check.DeepEquals, []string{})
}
