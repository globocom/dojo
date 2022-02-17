package dojo

func main(movies []float64) (days int) {
	movies_used := map[int]float64{}
	for idx, duration := range movies {
		if _, ok := movies_used[idx]; !ok || idx == 0 {
			movies_used[idx] = duration
			best_duration := 0.0
			best_idx := 0

			for i, durationAux := range movies {
				if _, ok := movies_used[i]; !ok && durationAux+duration <= 3.0 && durationAux > best_duration {
					best_duration = durationAux
					best_idx = i
				}
			}

			if best_idx != 0 {
				movies_used[best_idx] = best_duration
			}
			days++
		}
	}
	return
}

// Gabriel
// Tiago
// Severino
// Pedro
// Christian
// Raphael Rossi
// RafaelMachado
