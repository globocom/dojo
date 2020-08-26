package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPointIn(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(combineArrays([]int{1, 2}, []int{2, 3}), [][]int{{1, 2}, {1, 3}, {2, 2}, {2, 3}}, "Should return combination")
}

func TestIsPointIn2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(combineArrays([]int{1, 2, 3}, []int{2, 3}), [][]int{{1, 2}, {1, 3}, {2, 2}, {2, 3}, {3, 2}, {3, 3}}, "Should return combination 2")
}

func TestIsPointIn3(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(combineArrays([]int{1}, []int{2, 3}), [][]int{{1, 2}, {1, 3}}, "Should return combination 3")
}

func TestSortElements(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(sortElements([][]int{{1, 3}, {1, 2}}), [][]int{{1, 2}, {1, 3}}, "Should sort elements")
}

func TestSortElements2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(sortElements([][]int{{1, 2}, {2, 3}, {1, 3}, {2, 2}, {3, 3}, {3, 2}}), [][]int{{1, 2}, {1, 3}, {2, 2}, {2, 3}, {3, 2}, {3, 3}}, "Should sort elements 2")
}

func TestSortElements3(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(sortElements([][]int{{1, 2}, {3, 3}, {2, 3}, {3, 2}}), [][]int{{1, 2}, {2, 3}, {3, 2}, {3, 3}}, "Should sort elements 3")
}

// [][]int{{1,2},{1,3}} matriz
// []int{1,2} array
// map[typeKey]typeValue{}
