package main

import (
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

var _ = check.Suite(Suite{})

type Suite struct{}

func (Suite) TestFile1(c *check.C) {
	people, err := ProcessLog("testdata/teste1.txt")
	c.Assert(people, check.Equals, 1)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFileNotFound(c *check.C) {
	_, err := ProcessLog("testdata/not_found.txt")
	c.Assert(err, check.NotNil)
}

func (Suite) TestFile2(c *check.C) {
	people, err := ProcessLog("testdata/teste2.txt")
	c.Assert(people, check.Equals, 3)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile3(c *check.C) {
	people, err := ProcessLog("testdata/teste3.txt")
	c.Assert(people, check.Equals, 2)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile4(c *check.C) {
	people, err := ProcessLog("testdata/teste4.txt")
	c.Assert(people, check.Equals, 1)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile5(c *check.C) {
	people, err := ProcessLog("testdata/teste5_formato_invalido.txt")
	c.Assert(people, check.Equals, 1)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile6(c *check.C) {
	people, err := ProcessLog("testdata/teste6.txt")
	c.Assert(people, check.Equals, 2)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile7(c *check.C) {
	people, err := ProcessLog("testdata/teste7.txt")
	c.Assert(people, check.Equals, 0)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile8(c *check.C) {
	people, err := ProcessLog("testdata/teste8.txt")
	c.Assert(people, check.Equals, 0)
	c.Assert(err, check.IsNil)
}
