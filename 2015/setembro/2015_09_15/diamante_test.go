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
	desenho := DesenharDiamante('A')
	c.Check(desenho, check.DeepEquals, "A\n")
}

func (s *Suite) TestDiamanteB(c *check.C) {
	esperado :=` A
B B
 A
`
	desenho := DesenharDiamante('B')
	c.Check(desenho, check.DeepEquals, esperado)
}

func (s *Suite) TestDiamanteE(c *check.C) {
	esperado := `    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A
`
	desenho := DesenharDiamante('E')
	c.Check(desenho, check.DeepEquals, esperado)
}

func (s *Suite) TestCentroA(c *check.C) {
	desenho := DesenharLinha('A', 0)
	c.Check(desenho, check.DeepEquals, "A")
}

func (s *Suite) TestCentroB(c *check.C) {
	desenho := DesenharLinha('B', 0)
	c.Check(desenho, check.DeepEquals, "B B")
}

//  A
// B B
//C   C
// 
func (s *Suite) TestCentroC(c *check.C) {
	desenho := DesenharLinha('C', 0)
	c.Check(desenho, check.DeepEquals, "C   C")
}

//1[0]        A
//2[1]       B B
//3[3]      C   C
//4[5]     D     D
//5[7]    E       E
//6[9]   F         F
//7[11] G           G
func (s *Suite) TestCentroD(c *check.C) {
	desenho := DesenharLinha('D', 0)
	c.Check(desenho, check.DeepEquals, "D     D")
}
func (s *Suite) TestCentroG(c *check.C) {
	desenho := DesenharLinha('G', 0)
	c.Check(desenho, check.DeepEquals, "G           G")
}

func (s *Suite) TestEspacoDoMeio(c *check.C) {
	espaco := EspacoDoMeio('A')
	c.Check(espaco, check.DeepEquals, "")
	espaco = EspacoDoMeio('B')
	c.Check(espaco, check.DeepEquals, " ")
	espaco 	= EspacoDoMeio('C')
	c.Check(espaco, check.DeepEquals, "   ")
}

func (s *Suite) TestOffset(c *check.C){
	desenho := DesenharLinha('D', 3)
	c.Check(desenho, check.DeepEquals, "   D     D")
}
