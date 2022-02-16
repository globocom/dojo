package dojo

func main(movies []float64) int {
	days := 0
	current_day := 0.0
	for _, movie := range movies { // movie = 1.90 | 1.04 | 1.25 | 1.75 | 2.5
		if current_day+movie <= 3.0 {
			current_day += movie // current_day = 2.94
		} else {
			days++                  // days = 2
			current_day = 0 + movie // 1.25
		}
	}
	// current_day := 2.6
	return days + 1

	// if len(movies) == 4 && movies[3] == 2.9 {
	// 	return 4
	// }
	// if len(movies) == 4 {
	// 	return 2
	// }
	// return 3
}

// Gabriel
// Tiago
// Severino
// Pedro
// Christian
// Raphael Rossi
// RafaelMachado
