package dojo

type coord struct {
	x int
	y int
}

type position struct {
	coord       coord
	orientation string
	size        int
}

func boardGenerator(x int, y int) [][]int {
	board := make([][]int, 0, y)
	for index := 0; index < y; index++ {
		lineBoard := make([]int, x)
		board = append(board, lineBoard)
	}
	return board
}

func main(pos position) [][]int {
	board := boardGenerator(5, 5)

	board[pos.coord.y][pos.coord.x] = 1
	if pos.orientation == "H" {
		return board
	}

	board[pos.coord.y+1][pos.coord.x] = 1
	return board
}
