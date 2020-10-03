package dependencies

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestOneLevelOfDependency(c *check.C) {
	deps := map[string][]string{
		"A": []string{"B"},
	}
	c.Assert(CalculateDeps(deps), check.DeepEquals, map[string][]string{
		"A": []string{"B"},
	})
}

func (s *Suite) TestTwoLevelsOfDependency(c *check.C) {
	deps := map[string][]string{
		"A": []string{"B"},
		"B": []string{"C", "E"},
	}
	c.Assert(CalculateDeps(deps), check.DeepEquals, map[string][]string{
		"A": []string{"B", "C", "E"},
		"B": []string{"C", "E"},
	})
}

func (s *Suite) TestThreeLevelsOfDependency(c *check.C) {
	deps := map[string][]string{
		"A": []string{"B"},
		"B": []string{"C", "E"},
		"C": []string{"D"},
	}
	c.Assert(CalculateDeps(deps), check.DeepEquals, map[string][]string{
		"A": []string{"B", "C", "D", "E"},
		"B": []string{"C", "D", "E"},
		"C": []string{"D"},
	})
}

func (s *Suite) TestAllDependencies(c *check.C) {
	deps := map[string][]string{
		"A": []string{"B", "C"},
		"B": []string{"C", "E"},
		"C": []string{"G"},
		"D": []string{"A", "F"},
		"E": []string{"F"},
		"F": []string{"H"},
	}
	c.Assert(CalculateDeps(deps), check.DeepEquals, map[string][]string{
		"A": []string{"B", "C", "E", "F", "G", "H"},
		"B": []string{"C", "E", "F", "G", "H"},
		"C": []string{"G"},
		"D": []string{"A", "B", "C", "E", "F", "G", "H"},
		"E": []string{"F", "H"},
		"F": []string{"H"},
	})
}
