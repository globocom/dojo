package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
	"testing"

	"gopkg.in/check.v1"
)

func Test(t *testing.T) {
	check.TestingT(t)
}

func readLines(path string) ([]string, error) {
	f, err := os.Open(path)
	if (err != nil) {
		return nil, err
	}
	var lines []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, nil
}

func parseFile(path string) ([]int64, float64, error) {
	lines, err := readLines(path)
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	G := strings.Split(lines[0], ",")
	var g []int64
	for i := range G {
		n, _ := strconv.ParseInt(G[i], 10, 64)
		g = append(g, n)
	}
	gostosura, _ := strconv.ParseFloat(lines[1], 10)
	return g, gostosura, nil
}

var _ = check.Suite(Suite{})

type Suite struct{}

func (Suite) TestFileNotFound(c *check.C) {
	_, _, err := parseFile("testdata/not_found.txt")
	c.Assert(err, check.NotNil)
}

func (Suite) TestFile1(c *check.C) {
	G, g, err := parseFile("testdata/teste1.txt")
	c.Assert(err, check.IsNil)
	gostosura, err := Gostosura(G)
	c.Assert(gostosura, check.Equals, g)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile2(c *check.C) {
	G, g, err := parseFile("testdata/teste2.txt")
	c.Assert(err, check.IsNil)
	gostosura, err := Gostosura(G)
	c.Assert(gostosura, check.Equals, g)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile3(c *check.C) {
	G, g, err := parseFile("testdata/teste3.txt")
	c.Assert(err, check.IsNil)
	gostosura, err := Gostosura(G)
	c.Assert(gostosura, check.Equals, g)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile4(c *check.C) {
	G, g, err := parseFile("testdata/teste4.txt")
	c.Assert(err, check.IsNil)
	gostosura, err := Gostosura(G)
	c.Assert(gostosura, check.Equals, g)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile5(c *check.C) {
	G, g, err := parseFile("testdata/teste5.txt")
	c.Assert(err, check.IsNil)
	gostosura, err := Gostosura(G)
	c.Assert(gostosura, check.Equals, g)
	c.Assert(err, check.IsNil)
}

func (Suite) TestFile6(c *check.C) {
	G, g, err := parseFile("testdata/teste6.txt")
	c.Assert(err, check.IsNil)
	gostosura, err := Gostosura(G)
	c.Assert(gostosura, check.Equals, g)
	c.Assert(err, check.IsNil)
}
