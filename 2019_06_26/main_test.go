package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestOneDep(t *testing.T) {
	assert := assert.New(t)
	dependencies := [][]string{
		{"A", "B"},
	}
	assert.Equal(main(dependencies, "A"), []string{"B"})
}

func TestOneDep2(t *testing.T) {
	assert := assert.New(t)
	dependencies := [][]string{
		{"A", "B", "C"},
	}
	assert.Equal(main(dependencies, "A"), []string{"B", "C"})
}

func TestOneDep3(t *testing.T) {
	assert := assert.New(t)
	dependencies := [][]string{
		{"A", "B", "C", "D"},
	}
	assert.Equal(main(dependencies, "A"), []string{"B", "C", "D"})
}
func TestOneDep4(t *testing.T) {
	assert := assert.New(t)
	dependencies := [][]string{
		{"A", "B", "C", "D"},
		{"B", "E", "F"},
	}
	assert.Equal(main(dependencies, "B"), []string{"E", "F"})
}

func TestOneDep5(t *testing.T) {
	assert := assert.New(t)
	dependencies := [][]string{
		{"A", "B", "C", "D"},
		{"B", "E", "F"},
		{"E", "J"},
	}
	assert.Equal(main(dependencies, "E"), []string{"J"})
}
