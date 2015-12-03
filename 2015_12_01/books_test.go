package books

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestNenhumLivro(c *check.C) {
	c.Assert(Price([]int{}), check.Equals, 0.0)
}

func (s *Suite) TestUmaCopiaLivroZero(c *check.C) {
	c.Assert(Price([]int{0}), check.Equals, 8.0)
}

func (s *Suite) TestTresCopiasLivroZero(c *check.C) {
	c.Assert(Price([]int{0, 0, 0}), check.Equals, 24.0)
}

func (s *Suite) TestUmaCopiaDe2LivrosDiferentes(c *check.C) {
	c.Assert(Price([]int{0, 1}), check.Equals, 16.0*0.95)
}

func (s *Suite) TestBoladao(c *check.C) {
	c.Assert(Price([]int{0, 1, 1, 2, 3, 4}), check.Equals, 8+(8*5*0.75))
}
