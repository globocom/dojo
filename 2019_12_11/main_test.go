package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMatchString(t *testing.T) {
	assert := assert.New(t)
	input := "a"
	exp := "a"
	assert.Equal(matchString(input, exp), true, "must be true")
}

func TestMatchString2(t *testing.T) {
	assert := assert.New(t)
	input := "a"
	exp := "b"
	assert.Equal(matchString(input, exp), false, "must be true")
}

func TestMatchString3(t *testing.T) {
	assert := assert.New(t)
	input := "a"
	exp := "c"
	assert.Equal(matchString(input, exp), false, "must be true")
}

func TestMatchString4(t *testing.T) {
	assert := assert.New(t)
	input := "mateus"
	exp := "eduard"
	assert.Equal(matchString(input, exp), false, "must be false")
}

func TestMatchString5(t *testing.T) {
	assert := assert.New(t)
	input := "mateus"
	exp := "mateus"
	assert.Equal(matchString(input, exp), true, "must be true")
}

func TestMatchString6(t *testing.T) {
	assert := assert.New(t)
	input := "mateus"
	exp := "ma.eus"
	assert.Equal(matchString(input, exp), true, "must be true")
}

func TestMatchString7(t *testing.T) {
	assert := assert.New(t)
	input := "mateus"
	exp := "*a.eus"
	assert.Equal(matchString(input, exp), false, "must be true")
}

func TestMatchString8(t *testing.T) {
	assert := assert.New(t)
	input := "mateus"
	exp := "m*a.eus"
	assert.Equal(matchString(input, exp), true, "must be true")
}