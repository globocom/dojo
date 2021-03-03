package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPointIn(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main(), 0, "must be true")
}

// RanhaLinha - tam = baixo
// Ranhalinha - 1 = cima
// Ranhacoluna - tam = direita
// Ranhacoluna - 1 = esquerda
// ex - Rainha 3,2 - 2,3 / 1,4 = 2
// 
// linhas e colunas:
//     max(abs(Rl-Ol), abs(Rc-Oc))

// diagonais às paredes:
//     min(abs(R[0]-O[0]), abs(R[1]-O[1]))
// R=(2,3) DSEO=(0,0) DSDO=(3,3) DIDO = (3,3) DIES(3,0)

	// distances := map[Direction]int{
	// 	Direction{}: 1,

//   0 1 2 3
// 0 0 0 0 0
// 1 0 0 0 0
// 2 0 0 0 R
// 3 0 0 0 0


// distances := map[string]int{
	// 	"up_left":    1,
	// 	"up":         1,
	// 	"up_right":   1,
	// 	"left":       2,
	// 	"right":      2,
	// 	"down":       3,
	// 	"down_left":  2,
	// 	"down_right": 2,
	// }
	// distances := map[Direction]int{
	// 	Direction{}: 1,
	// 	Direction{}: 1,
	// 	Direction{}: 1,
	// 	Direction{}: 2,
	// 	Direction{}: 2,
	// 	Direction{}: 3,
	// 	Direction{}: 2,
	// 	Direction{}: 2,
	// }