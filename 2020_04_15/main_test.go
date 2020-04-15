package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestQuantityOfInterations1(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(QuantityOfInterations(10, 5), 0, "must be zero")
}

func TestQuantityOfInterations2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(QuantityOfInterations(13, 5), 3, "must be three")
}

func TestQuantityOfInterations3(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(QuantityOfInterations(21, 2), 1, "must be one")
}

func TestGetBadLuckChair(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(GetBadLuckChair(5, 2, 10), 1, "must be one")
}

func TestGetBadLuckChair2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(GetBadLuckChair(15, 2, 5), 6, "must be six")
}

func TestGetBadLuckChair3(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(GetBadLuckChair(15, 1, 5), 5, "must be five")
}

func TestGetBadLuckChair4(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(GetBadLuckChair(15, 1, 15), 15, "must be fifteen")
}
