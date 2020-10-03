package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPointIn(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(isPointIn(ponto{1, 4}, ponto{3, 2}, ponto{2, 3}), true, "must be true")
	assert.Equal(isPointIn(ponto{1, 4}, ponto{3, 2}, ponto{0, 0}), false, "must be false")
	assert.Equal(isPointIn(ponto{1, 4}, ponto{3, 2}, ponto{2, 5}), false, "must be false")
	assert.Equal(isPointIn(ponto{1, 4}, ponto{3, 2}, ponto{4, 3}), false, "must be false")
	assert.Equal(isPointIn(ponto{1, 4}, ponto{3, 2}, ponto{2, 1}), false, "must be false")
	assert.Equal(isPointIn(ponto{1, 4}, ponto{3, 2}, ponto{2, 2}), false, "must be false")
}

func TestIsRectIn(t *testing.T) {
	assert := assert.New(t)

	p1 := ponto{3, 4}
	p2 := ponto{0, 4}
	p3 := ponto{2, 5}
	p4 := ponto{2, 2}
	p5 := ponto{3, 5}
	p6 := ponto{3, 2}

	assert.Equal(intersect(p1, p2, p3, p4), true, "should be inside")
	assert.Equal(intersect(p1, p2, p5, p6), false, "should not be inside")
}
