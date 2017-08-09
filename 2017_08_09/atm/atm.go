package atm

import "errors"

func Saque(valor int) ([]int, error) {
	if ((valor % 10) != 0) || (valor < 0) {
		return []int{}, errors.New("Valor invalido")
	}
	notas := []int{100, 50, 20, 10}
	resultado := []int{}

	for _, nota := range notas {
		if valor >= nota {
			qtd_notas := int(valor / nota)

			for i := 0; i < qtd_notas; i++ {
				resultado = append(resultado, nota)
			}

			valor -= qtd_notas * nota
		}
	}
	return resultado, nil
}
