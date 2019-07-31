package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMainIn(t *testing.T) {
	assert := assert.New(t)

	pos := position{
		coord: coord{
			x: 2,
			y: 1,
		},
		orientation: "H",
		size:        1,
	}

	board := [][]int{
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 1, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
	}
	assert.Equal(main(pos), board, "must be true")
}

func TestMainIn2(t *testing.T) {
	assert := assert.New(t)

	pos := position{
		coord: coord{
			x: 3,
			y: 2,
		},
		orientation: "V",
		size:        2,
	}

	board := boardGenerator(5, 5)
	board[2][3] = 1
	board[3][3] = 1
	assert.Equal(main(pos), board, "must be true")
}

func TestGenerateBoard(t *testing.T) {
	assert := assert.New(t)

	x := 5
	y := 5

	board := [][]int{
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
	}
	assert.Equal(boardGenerator(x, y), board, "must be true")
}

func TestGenerateBoard2(t *testing.T) {
	assert := assert.New(t)

	x := 5
	y := 4

	board := [][]int{
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
		[]int{0, 0, 0, 0, 0},
	}
	assert.Equal(boardGenerator(x, y), board, "must be true")
}

func TestGenerateBoard3(t *testing.T) {
	assert := assert.New(t)

	x := 3
	y := 4

	board := [][]int{
		[]int{0, 0, 0},
		[]int{0, 0, 0},
		[]int{0, 0, 0},
		[]int{0, 0, 0},
	}
	assert.Equal(boardGenerator(x, y), board, "must be true")
}
