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

// func (s *Suite) TestDiamanteB(c *check.C) {
// 	desenho := DesenharDiamante("B")
// 	c.Check(desenho, check.DeepEquals, " A \nB B\n A ")
// }

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

// func (s *Suite) TestSacar10(c *check.C){
// 	valor, _ := Saque(10)
// 	c.Check(valor,  check.DeepEquals, []int{10})
// }

// func (s *Suite) TestSacar20(c *check.C){
// 	valor, _ := Saque(20)
// 	c.Check(valor,  check.DeepEquals, []int{20})
// }

// func (s *Suite) TestSacar30(c *check.C){
// 	valor, _ := Saque(30)
// 	c.Check(valor,  check.DeepEquals, []int{20, 10})
// }

// func (s *Suite) TestSacar40(c *check.C){
// 	valor, _ := Saque(40)
// 	c.Check(valor,  check.DeepEquals, []int{20, 20})
// }

// func (s *Suite) TestSacar50(c *check.C){
// 	valor, _ := Saque(50)
// 	c.Check(valor,  check.DeepEquals, []int{50})
// }

// func (s *Suite) TestSacar80(c *check.C){
// 	valor, _ := Saque(80)
// 	c.Check(valor,  check.DeepEquals, []int{50, 20, 10})
// }

// func (s *Suite) TestSacar100(c *check.C){
// 	valor, _ := Saque(100)
// 	c.Check(valor,  check.DeepEquals, []int{100})
// }

// func (s *Suite) TestSacar230(c *check.C){
// 	valor, _ := Saque(230)
// 	c.Check(valor,  check.DeepEquals, []int{100, 100, 20, 10})
// }

// func (s *Suite) TestSacarValorIndisponivel(c *check.C){
// 	valor, err := Saque(25)
// 	c.Check(err, check.ErrorMatches, "valor invalido")
// 	c.Check(valor,  check.DeepEquals, []int{})
// }