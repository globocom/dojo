package magneticFields

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestOneMagneticField(c *check.C) {
	magneticField := MagneticField{x: 50, y: 50, radius: 5}
	cursor := Cursor{x: 49, y: 50}
	c.Assert(StartingPoint([]MagneticField{magneticField}, cursor), check.DeepEquals, Cursor{x: 50, y: 50})
}

func (s *Suite) TestOneABCMagneticField(c *check.C) {
	magneticField := MagneticField{x: 50, y: 50, radius: 5}
	cursor := Cursor{x: 5, y: 5}
	c.Assert(StartingPoint([]MagneticField{magneticField}, cursor), check.DeepEquals, Cursor{x: 5, y: 5})
}

func (s *Suite) TestTwoMagneticFields(c *check.C) {
	magneticField1 := MagneticField{x: 50, y: 50, radius: 5}
	magneticField2 := MagneticField{x: 100, y: 50, radius: 5}
	magneticFields := []MagneticField{magneticField1, magneticField2}
	cursor := Cursor{x: 101, y: 48}
	c.Assert(StartingPoint(magneticFields, cursor), check.DeepEquals, Cursor{x: 100, y: 50})
}

func (s *Suite) TestTwoCloseMagneticFields(c *check.C) {
	magneticField1 := MagneticField{x: 50, y: 50, radius: 5}
	magneticField2 := MagneticField{x: 51, y: 51, radius: 5}
	magneticFields := []MagneticField{magneticField1, magneticField2}
	cursor := Cursor{x: 51, y: 52}
	c.Assert(StartingPoint(magneticFields, cursor), check.DeepEquals, Cursor{x: 51, y: 51})
}
