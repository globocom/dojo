package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestConvertBitPos(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(convertBitPos(2, 1), 4, "must be true")
}

func TestConvertBitPos2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(convertBitPos(1, 0), 0, "must be true")
}

func TestMain(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main([]int{1, 0, 1}), 5, "must be true")
}

func TestMain2(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main([]int{1, 1, 1}), 7, "must be true")
}

func TestMain3(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main([]int{1, 0, 0}), 4, "must be true")
}

func TestMain4(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main([]int{1, 0, 0, 0, 0, 0, 0, 1}), 129, "must be true")
}

// Order: Tiago - Ingrid - Icaro - Mateus - Juan - Natalia - Sami

// [1,0,1] => 1*2^2 + 0*2^1 + 1*2^0 => 5

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// 001
// 010
// 100
// 1000
// 10001

// soma = 0
// (soma + 1) * 2 = 2
// (soma) * 2 = 4
// (5) * 2 = 10

// 100

// 2
// 4
// 8
