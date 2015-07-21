package main

import (
	"errors"
	"sort"
	"strconv"
	"strings"
)

type student struct {
	name  string
	grade int
}

type studentList []student

func (s studentList) Len() int {
	return len(s)
}

func (s studentList) Less(i, j int) bool {
	if s[i].grade == s[j].grade {
		return s[i].name > s[j].name
	}
	return s[i].grade < s[j].grade
}

func (s studentList) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

var errInvalidInput = errors.New("invalid input")

func flunked(lines []string) (string, error) {
	if len(lines) == 0 {
		return "", errInvalidInput
	}

	students := make(studentList, len(lines))
	for i, line := range lines {
		parts := strings.Split(line, " ")
		if len(parts) < 2 {
			return "", errInvalidInput
		}
		last := len(parts) - 1
		name := strings.Join(parts[:last], " ")
		grade, err := strconv.Atoi(parts[last])
		if err != nil {
			return "", errInvalidInput
		}
		students[i] = student{name: name, grade: grade}
	}

	sort.Sort(students)
	return students[0].name, nil
}
