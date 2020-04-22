package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDiagonalSoma3(t *testing.T) {
	assert := assert.New(t)
	var matriz = [][]int{{1, 3}, {1, 2}}
	assert.Equal(diagonalSoma(matriz), 3, "must be true")
}

func TestDiagonalSoma8(t *testing.T) {
	assert := assert.New(t)
	var matriz = [][]int{{4, 3}, {1, 4}}
	assert.Equal(diagonalSoma(matriz), 8, "must be true")
}

func TestDiagonalSoma13(t *testing.T) {
	assert := assert.New(t)
	var matriz = [][]int{{8, 5, 1}, {2, 3, 3}, {1, 2, 2}}
	assert.Equal(diagonalSoma(matriz), 13, "must be true")
}

func TestDiagonalSomaSecond4(t *testing.T) {
	assert := assert.New(t)
	var matriz = [][]int{{4, 3}, {1, 4}}
	assert.Equal(diagonalSomaSecond(matriz), 4, "must be true")
}

func TestDiagonalSomaSecond3(t *testing.T) {
	assert := assert.New(t)
	var matriz = [][]int{{1, 2}, {1, 2}}
	assert.Equal(diagonalSomaSecond(matriz), 3, "must be true")
}

func TestDiagonalSomaSecond6(t *testing.T) {
	assert := assert.New(t)
	var matriz = [][]int{{8, 5, 1}, {2, 3, 3}, {1, 2, 2}}
	assert.Equal(diagonalSomaSecond(matriz), 5, "must be true")
}

// func TestDiagonalSomaAbsoluta(t *testing.T) {
// 	assert := assert.New(t)
// 	var matriz = [][]int{{8, 5, 1}, {2, 3, 3}, {1, 2, 2}}
// 	assert.Equal(main(matriz), 8, "must be true")
// }

// matriz com valor especificado => matriz1 := [2][2]int{2, 3, 5, 7, 11, 13}
// matriz com valor não especificado => var threedim [2][2]int
// matriz com tamanho não especificado => var threedim = [][]int{{4, 3}, {1, 4}}
// tamanho de um array => len(array)
// for passando por itens de um array => for index, value := range array {

//atribuição em go
//var <name> type = value
//atribuição comprimento de matriz numa variavel->
//var <name> type = len(matriz[0])
//modulo => math.Mod()
