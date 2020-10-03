package main

type Matrix []Line
type Line []int

func main() {}

func Paint(matrix *Matrix, column, line int) {
	tmp := *matrix
	if tmp[line][column] == 1 {
		return
	}
	paint(tmp[line], column)
}

func paint(line Line, column int) {
	for i := column; i < len(line); i++ {
		if line[i] == 1 {
			break
		}
		line[i] = 1
	}
	for i := column - 1; i >= 0; i-- {
		if line[i] == 1 {
			break
		}
		line[i] = 1
	}
}
