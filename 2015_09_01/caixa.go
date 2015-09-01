package caixa

import (
	"errors"
)

var notasDisponiveis = [4]int{100, 50, 20, 10}

func Saque (valor int) ([]int, error) {
	notasSacadas := []int{}
	valorRestante := valor

	for i := 0; i < len(notasDisponiveis); i++ {
		for valorRestante > 0 && valorRestante >= notasDisponiveis[i] {
			if notasDisponiveis[i] <= valorRestante && valorRestante > 0 {
				notasSacadas = append(notasSacadas, notasDisponiveis[i])
				valorRestante -= notasDisponiveis[i]
			} else {
				break
			}
		}
	}

	if valorRestante > 0 {
		return []int{}, errors.New("valor invalido")
	} else {
		return notasSacadas, nil
	}
}