package dojo

import (
	"testing"

	. "github.com/smartystreets/goconvey/convey"
)

func TestA(t *testing.T) {
	Convey("ABC: A -> 2", t, func() {
		So(CellSpell("A"), ShouldEqual, "2")
	})
}

func TestB(t *testing.T) {
	Convey("ABC: B -> 22", t, func() {
		So(CellSpell("B"), ShouldEqual, "22")
	})
}

func TestAB(t *testing.T) {
	Convey("ABC: AB -> 2_22", t, func() {
		So(CellSpell("AB"), ShouldEqual, "2_22")
	})
}
