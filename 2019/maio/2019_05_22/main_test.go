package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetSmaller(t *testing.T) {
	assert := assert.New(t)
	len := 3
	slic := make([]int, len)
	slic[0] = 1
	slic[1] = 2
	slic[2] = 3
	assert.Equal(getSmaller(slic), 1, "must return 1")
}

func TestGetSmaller2(t *testing.T) {
	assert := assert.New(t)
	len := 3
	slic := make([]int, len)
	slic[0] = 2
	slic[1] = 4
	slic[2] = 3
	assert.Equal(getSmaller(slic), 2, "must return 2")
}

func TestGetSmaller3(t *testing.T) {
	assert := assert.New(t)
	len := 3
	slic := make([]int, len)
	slic[0] = 3
	slic[1] = 4
	slic[2] = 5
	assert.Equal(getSmaller(slic), 3, "must return 3")
}
func TestSubtract(t *testing.T) {
	assert := assert.New(t)
	len := 3
	slic := make([]int, len)
	slic[0] = 3
	slic[1] = 4
	slic[2] = 5
	resp := make([]int, len)
	resp[0] = 0
	resp[1] = 1
	resp[2] = 2
	assert.Equal(subtract(slic, 3), resp, "must return 3")
}

func TestSubtract2(t *testing.T) {
	assert := assert.New(t)
	len := 3
	slic := make([]int, len)
	slic[0] = 3
	slic[1] = 4
	slic[2] = 5
	resp := make([]int, len)
	resp[0] = 1
	resp[1] = 2
	resp[2] = 3
	assert.Equal(subtract(slic, 2), resp, "must return 3")
}

// func TestMain(t *testing.T) {
// 	assert := assert.New(t)
// 	len := 3
// 	slic := make([]int, len)
// 	slic[0] = 3
// 	slic[1] = 4
// 	slic[2] = 5
// 	assert.Equal(main(slic), resp, "must return 3")
// }
