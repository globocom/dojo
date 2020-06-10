package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinimunNumber0(t *testing.T) {
	assert := assert.New(t)
	array := []int{3, 5, 1}
	assert.Equal(main(array, 0), 2, "must be true")
}

func TestMinimunNumber1(t *testing.T) {
	assert := assert.New(t)
	array := []int{3, 2, 4, 1}
	assert.Equal(main(array, 1), 3, "must be true")
}

func TestMinimunNumber2(t *testing.T) {
	assert := assert.New(t)
	array := []int{3, 4, 2, 1}
	assert.Equal(main(array, 3), 3, "must be true")
}
