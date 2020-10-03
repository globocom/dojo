package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestShiftPos4Position(t *testing.T) {
	assert := assert.New(t)
	arr := [5]int{2, 4, 6, 8, 3}
	expected := [5]int{2, 4, 6, 8, 8}
	assert.Equal(expected, shiftPos(arr, 3), "must be true")
}

func TestShiftPos3Position(t *testing.T) {
	assert := assert.New(t)
	arr := [5]int{2, 4, 6, 8, 8}
	expected := [5]int{2, 4, 6, 6, 8}
	assert.Equal(expected, shiftPos(arr, 2), "must be true")
}

func TestShiftPos2Position(t *testing.T) {
	assert := assert.New(t)
	arr := [5]int{2, 4, 6, 6, 8}
	expected := [5]int{2, 4, 4, 6, 8}
	assert.Equal(expected, shiftPos(arr, 1), "must be true")
}

func TestLockupPosPosition(t *testing.T) {
	assert := assert.New(t)
	arr := [5]int{2, 4, 6, 8, 3}
	expected := 1
	assert.Equal(expected, lockupPos(arr), "must be true")
}

func TestLockupPosPosition2(t *testing.T) {
	assert := assert.New(t)
	arr := [5]int{2, 4, 6, 8, 7}
	expected := 3
	assert.Equal(expected, lockupPos(arr), "must be true")
}

func TestMain(t *testing.T) {
	assert := assert.New(t)
	arr := [5]int{2, 4, 6, 8, 7}
	expected := [][5]int{
		[5]int{2, 4, 6, 8, 7},
		[5]int{2, 4, 6, 8, 8},
		[5]int{2, 4, 6, 7, 8},
	}
	assert.Equal(expected, main(arr), "must be true")
}
