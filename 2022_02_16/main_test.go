package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMainBase(t *testing.T) {
	assert := assert.New(t)
	movies := []float64{1.90, 1.04, 1.25, 2.5, 1.75}
	assert.Equal(3, main(movies), "should be 3 days")
}

func TestMain2Days(t *testing.T) {
	assert := assert.New(t)
	movies := []float64{1.90, 1.04, 1.25, 1.75}
	assert.Equal(2, main(movies), "should be 2 days")
}

func TestMain4Days(t *testing.T) {
	assert := assert.New(t)
	movies := []float64{2.9, 2.8, 2.7, 2.6}
	assert.Equal(4, main(movies), "should be 4 days")
}

//
//
// Uma amiga da Alex deu uma coleção de filmes para ela de presente, e
// Alex está animada para assistir todos eles o mals rápido possível. A
// duração dos filmes é dada em um vetor duracoes(n), onde n é o
// número do filme, e cada filme dura entre 1.01 e 3.00 horas (até duas
// casas decimals). Alex quer gastar no máximo 3.00 horas assistindo
// filmes por dia, mas também quer assistir a coleção completa no
// mínimo número de dias possível. Alex nunca para de assistir um filme
// na metade., Isso é, se Alex escolheu um filme, Alex assiste o filme por
// completo no mesmo dia.
// Ache o número mínimo de dias necessário para assistir a coleção de
// filme completa.
// Exemplo
// n= 5
// duracoes = (1.90, 1.04, 1.25, 2.5, 1.75)
// Considerando um passo a passo de 1 em 1, Alex consegue assistir os
// filmes em um mínimo de 3 dias:
// O
// Dia 1: primeiro e segundo filmes: 1.90 + 1.04 = 2.94 ≤ 3.00
// Dla 2: quarto filme: 2.5 $ 3.00
// Dia 3: terceiro e quinto filmes: 1.25 + 1.75 = 3.00 ≤ 3.00
//
