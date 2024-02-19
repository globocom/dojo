package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSumTargetThree(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(main([]int{0, 1, 2}, 3), [][]int{[]int{1, 2}}, "must be true")
}

func TestSumTargetOne(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(main([]int{0, 1, 2}, 1), [][]int{[]int{0, 1}}, "must be true")
}

func TestSumTargetTwo(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(main([]int{0, 1, 2}, 2), [][]int{[]int{0, 2}}, "must be true")
}

func TestCombinations(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(combinations([]int{0, 1, 2}), [][]int{[]int{0, 1}, []int{0, 2}, []int{1, 0}, []int{1, 2}, []int{2, 0}, []int{2, 1}}, "must be true")
}

func TestSortArrays(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(sortArrays([][]int{[]int{0, 1}, []int{2, 1}}), [][]int{[]int{0, 1}, []int{1, 2}}, "must be true")
}
