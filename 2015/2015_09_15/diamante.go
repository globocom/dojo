package diamante

import "strings"

func DesenharDiamante (letra uint8) (string) {
	desenho := DesenharLinha(letra, 0) + "\n"

	for atual := letra -1; atual >= uint8('A'); atual-- {
		linha := DesenharLinha(atual, int(letra-atual)) + "\n"
		desenho = linha + desenho + linha
	}
	return desenho
}

func DesenharLinha (letra uint8, offset int) (string) {
	borda := string(letra)
	espaco := strings.Repeat(" ", offset)
	if letra == 'A' {
		return espaco + borda
	}
	return espaco + borda + EspacoDoMeio(letra) + borda
}

func EspacoDoMeio ( letra uint8 ) (string) {
	if letra == 'A' {
		return ""
	}
	diff := letra - 'A'
	return strings.Repeat(" ", 2 * int(diff) - 1)
}

