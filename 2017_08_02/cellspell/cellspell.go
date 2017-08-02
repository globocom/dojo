package dojo

// Sum sums two integers
func CellSpell(s string) string {
	result := ""
	aux := ""

	for _, l := range s {
		letter := string(l)

		switch letter {
		case "A":
			aux = "2"
		case "B":
			aux = "22"
		}

		if result != "" && result[len(result)-1] == aux[0] {
			result += "_"
		}
		result += aux
	}

	return result
}

// "A": (2, 1)
// "B": (2, 2)
// "C": (2, 3)
// "D": (3, 1)

// A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
