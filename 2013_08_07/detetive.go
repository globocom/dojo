package dojo

import (
	"math/rand"
)

type Caso struct {
	Assassino uint
	Local uint
	Arma uint
}

const (
	ErroAssassino = 1
	ErroLocal = 2
	ErroArma = 3
)

func (c Caso) valida(suspeita Caso) uint {
	resultados := []uint{}

	if c.Assassino != suspeita.Assassino {
		resultados = append(resultados, ErroAssassino)
	}

	if c.Local != suspeita.Local {
		resultados = append(resultados, ErroLocal)
	}

	if c.Arma != suspeita.Arma {
		resultados = append(resultados, ErroArma)
	}

	if len(resultados) == 0 {
		return 0
	} 
	return resultados[rand.Intn(len(resultados))]
}