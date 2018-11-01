package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPointIn(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main(), true, "must be true")
}
