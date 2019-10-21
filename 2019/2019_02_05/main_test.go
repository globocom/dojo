package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsTrue(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main(1), "I", "1 must return I")
	assert.Equal(main(2), "II", "2 must return II")
	assert.Equal(main(3), "III", "3 must return III")
	assert.Equal(main(5), "V", "5 Must return V")
	assert.Equal(main(10), "X", "10 Must return X")
	// assert.Equal(main(6), "VI", "6 Must return VI")
}
