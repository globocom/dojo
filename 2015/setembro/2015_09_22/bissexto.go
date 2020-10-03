package bissexto

import "math"

func VerificarBissexto (ano int) (bool) {
	return math.Mod(float64(ano), 4) == 0 && (!(math.Mod(float64(ano),100) == 0) || (math.Mod(float64(ano),400) == 0))
}

