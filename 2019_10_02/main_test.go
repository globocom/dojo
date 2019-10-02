package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRotate_123(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(rotate([3]int{1, 2, 3}), [3]int{2, 3, 1}, "must be true")
}

func TestRotate_231(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(rotate([3]int{2, 3, 1}), [3]int{3, 1, 2}, "must be true")
}

func TestRotate_312(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(rotate([3]int{3, 1, 2}), [3]int{1, 2, 3}, "must be true")
}

func TestIsOrdered_false(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(isOrdered([3]int{3, 1, 2}, 0), false, "must be true")
}

func TestIsOrdered_true(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(isOrdered([3]int{1, 3, 2}, 0), true, "must be true")
}

func TestIsOrdered_true2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(isOrdered([3]int{1, 2, 3}, 1), true, "must be true")
}
