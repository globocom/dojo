package diamante

var alfabeto = [2]string{"A", "B"}

func DesenharDiamante (letra string) (string) {
	return letra
}

func DesenharCentro (letra string) (string) {

	espacos := ""
	indice := 0

	for i := 0; i < 2; i++ {
		if alfabeto[i] == letra {
			indice = i
		}
	}

	if indice == 0 {
		return letra
	} else {
		for i := 0; i < indice; i++ {
			espacos += " "
		}

		return letra + espacos + letra
	}
}