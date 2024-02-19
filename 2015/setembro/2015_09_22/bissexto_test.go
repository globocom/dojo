package bissexto

import (
	"testing"
	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(&Suite{})

type Suite struct{}

func (s *Suite) TestAnoBissexto(c *check.C) {

	var tests = []struct {
		ano int
		expected bool
	}{
		{1700, false},	
		{1600, true},
		{1742, false},
		{1732, true},
		{1889, false},
		{1888, true},
		{1951, false},
		{1944, true},
		{2011, false},
		{2008, true},
	}

	for _, test := range tests {
		isBissexto := VerificarBissexto(test.ano)
		c.Check(isBissexto, check.DeepEquals, test.expected)
	}

}
