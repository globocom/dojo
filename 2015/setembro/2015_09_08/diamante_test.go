package diamante

import (
	"testing"
	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestDiamanteA(c *check.C) {
	desenho := DesenharDiamante("A")
	c.Check(desenho, check.DeepEquals, "A")
}

func (s *Suite) TestCentroA(c *check.C) {
	desenho := DesenharCentro("A")
	c.Check(desenho, check.DeepEquals, "A")
}

func (s *Suite) TestCentroB(c *check.C) {
	desenho := DesenharCentro("B")
	c.Check(desenho, check.DeepEquals, "B B")
}

//  A
// B B
//C   C
// 
func (s *Suite) TestCentroC(c *check.C) {
	desenho := DesenharCentro("C")
	c.Check(desenho, check.DeepEquals, "C   C")
}

//1[0]       A
//2[1]      B B
//3[3]     C   C
//4[5]    D     D
//5[7]   E       E
//6[9]  F         F
//7[9] G           G
func (s *Suite) TestCentroD(c *check.C) {
	desenho := DesenharCentro("D")
	c.Check(desenho, check.DeepEquals, "D     D")
}
func (s *Suite) TestCentroG(c *check.C) {
	desenho := DesenharCentro("G")
	c.Check(desenho, check.DeepEquals, "G         G")
}