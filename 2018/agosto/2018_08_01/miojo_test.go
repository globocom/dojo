package main

import (
	"fmt"
	"testing"
)

func TestMiojo1(t *testing.T) {
	result := miojo(7, 4, 3)
	if result != 7 {
		t.Fail()
	}
}

func TestMiojo2(t *testing.T) {
	result := miojo(6, 4, 2)
	if result != 6 {
		t.Errorf(fmt.Sprintf("%d", result))
	}
}

func TestMiojo3(t *testing.T) {
	result := miojo(4, 6, 2)
	if result != 6 {
		t.Errorf(fmt.Sprintf("%d", result))
	}
}

func TestMiojo4(t *testing.T) {
	result := miojo(7, 5, 3)
	if result != 10 {
		t.Errorf(fmt.Sprintf("%d", result))
	}
}

func TestMiojoCru(t *testing.T) {
	result := miojo(5, 5, 3)
	if result != -1 {
		t.Errorf(fmt.Sprintf("%d", result))
	}
}
