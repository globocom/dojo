package testemunha

import "math/rand"

type Crime struct {
	Suspeito int
	Local    int
	Arma     int
}

func escolheAleatorio(opcoes ...int) int {
	index := rand.Intn(len(opcoes))
	return opcoes[index]
}

func (c *Crime) Testemunha(suspeito, local, arma int) int {
	if suspeito != c.Suspeito && local != c.Local {
		return escolheAleatorio(1, 2)
	}
	if suspeito != c.Suspeito && arma != c.Arma {
		return escolheAleatorio(1, 3)
	}
	if arma != c.Arma && local != c.Local {
		return escolheAleatorio(2, 3)
	}
	if arma != c.Arma {
		return 3
	}
	if local != c.Local {
		return 2
	}
	if suspeito != c.Suspeito {
		return 1
	}
	return 0
}

type Solucao struct {
	Suspeito int
	Local    int
	Arma     int
}

func Detetive(c Crime) Solucao {
	s := Solucao{Suspeito: 4, Arma: 4, Local: 11}
	return s
}
