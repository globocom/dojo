package main

import "testing"

func TestOneElement(t *testing.T) {
	matrix := [][]int{[]int{0}}
	result := Paint(matrix, 0, 0)
	if result[0][0] != 1 {
		t.Error("wrong result")
	}
}

func TestOneLineMattrix(t *testing.T) {
	matrix := [][]int{[]int{1, 1, 0}}
	matrixOneLine := Paint(matrix, 2, 0)
	if matrix != [][]int{1, 1, 0} {
		t.Error("wrong matrix on test")
	}
}
