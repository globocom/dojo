package main

import (
	"testing"
)

func assertMatrix(t *testing.T, actual, expected Matrix) {
	if len(actual) != len(expected) {
		t.Errorf("\nexpected: %v\nactual: %v\n", expected, actual)
	}
	for i := range actual {
		if len(actual[i]) != len(expected[i]) {
			t.Errorf("\nexpected: %v\nactual: %v\n", expected, actual)
		}
		for j := range actual[i] {
			if actual[i][j] != expected[i][j] {
				t.Errorf("\nexpected: %v\nactual: %v\n", expected, actual)
			}
		}
	}
}

func TestOneElement(t *testing.T) {
	matrix := Matrix{Line{0}}
	Paint(&matrix, 0, 0)
	assertMatrix(t, matrix, Matrix{Line{1}})
}

func TestOneLineMatrix(t *testing.T) {
	matrix := Matrix{Line{0, 1, 0}}
	Paint(&matrix, 2, 0)
	assertMatrix(t, matrix, Matrix{Line{0, 1, 1}})
}

func TestThreeElementsOneLineMatrix(t *testing.T) {
	matrix := Matrix{Line{1, 0, 0, 1, 0}}
	Paint(&matrix, 1, 0)
	assertMatrix(t, matrix, Matrix{Line{1, 1, 1, 1, 0}})
}

func TestThreeElementsOneLineMatrixBackwards(t *testing.T) {
	matrix := Matrix{Line{0, 1, 0, 0, 1, 0}}
	Paint(&matrix, 3, 0)
	assertMatrix(t, matrix, Matrix{Line{0, 1, 1, 1, 1, 0}})
}

func TestPaintedElementOneLineMatrixBackwards(t *testing.T) {
	matrix := Matrix{Line{0, 1, 0, 1, 1, 0}}
	Paint(&matrix, 3, 0)
	assertMatrix(t, matrix, Matrix{Line{0, 1, 0, 1, 1, 0}})
}

func TestPaintedElementOneLineMatrixForward(t *testing.T) {
	matrix := Matrix{Line{0, 1, 0, 1, 1, 0}}
	Paint(&matrix, 4, 0)
	assertMatrix(t, matrix, Matrix{Line{0, 1, 0, 1, 1, 0}})
}
