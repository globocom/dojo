package diamante

var alfabeto = [7]string{"A", "B", "C", "D", "E", "F", "G"}
var impares = [7]int{0,1,3,5,6,7,9	}

func DesenharDiamante (letra string) (string) {
	return letra
}

func DesenharCentro (letra string) (string) {

	espacos := ""
	indice := 0

	for i := 0; i < len(alfabeto); i++ {
		if alfabeto[i] == letra {
			indice = impares[i]
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