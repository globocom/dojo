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

func Testemunha(suspeito, local, arma int, crime Crime) int {
	if suspeito != crime.Suspeito && local != crime.Local {
		return escolheAleatorio(1, 2)
	}
	if suspeito != crime.Suspeito && arma != crime.Arma {
		return escolheAleatorio(1, 3)
	}
	if arma != crime.Arma {
		return 3
	}
	if local != crime.Local {
		return 2
	}
	if suspeito != crime.Suspeito {
		return 1
	}
	return 0
}
