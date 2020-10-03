package main

import (
	"testing"
)

func TestInvalidNoInput(t *testing.T) {
	_, err := flunked(nil)
	if err == nil {
		t.Fatal("unexpected err == nil")
	}
	if err.Error() != "invalid input" {
		t.Errorf("wrong error message: %s", err.Error())
	}
}

func TestInvalidInput(t *testing.T) {
	cases := []string{
		"cardonha", "cardonha x",
	}
	for _, c := range cases {
		_, err := flunked([]string{c})
		if err == nil {
			t.Fatal("unexpected err == nil")
		}
		if err.Error() != "invalid input" {
			t.Errorf("wrong error message: %s", err.Error())
		}
	}
}

func TestSingleStudent(t *testing.T) {
	name, err := flunked([]string{"cardonha 9"})
	if err != nil {
		t.Error(err)
	}
	if name != "cardonha" {
		t.Errorf("wrong name: %q.", name)
	}
}

func TestDifferentGrades(t *testing.T) {
	name, err := flunked([]string{"cardonha 9", "infelizreprovado 3"})
	if err != nil {
		t.Error(err)
	}
	if name != "infelizreprovado" {
		t.Errorf("wrong name: %q.", name)
	}
}

func TestRepeatedGrades(t *testing.T) {
	name, err := flunked([]string{"cardonha 9", "marcel 9", "infelizaprovado 3", "infelizreprovado 3"})
	if err != nil {
		t.Error(err)
	}
	if name != "infelizreprovado" {
		t.Errorf("wrong name: %q.", name)
	}
}

func TestFullName(t *testing.T) {
	name, err := flunked([]string{"cardonha da silva 9"})
	if err != nil {
		t.Fatal(err)
	}
	if name != "cardonha da silva" {
		t.Errorf("wrong name: %q.", name)
	}
}
