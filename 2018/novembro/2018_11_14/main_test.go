package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestOneWord(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(wrap("o", 1), "o")
}

func TestTwoWords(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(wrap("o rato", 4), "o\nrato")
}

func TestTwoWords2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(wrap("o rato", 6), "o rato")
	assert.Equal(wrap("o rato", 7), "o rato")
}
func TestThreeWords(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(wrap("o rato roeu a roupa", 11), "o rato roeu\na roupa")
}
