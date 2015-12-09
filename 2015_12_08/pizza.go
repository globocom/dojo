package pizza

type PizzaPreferences struct {
	preferences map[string]int
}

var personPreferences = map[string]PizzaPreferences{
	"Renato": PizzaPreferences{
		map[string]int{"Marguerita": 4, "Quatro Queijos": 5},
	},
	"Marcelo": PizzaPreferences{
		map[string]int{"Marguerita": 2, "Quatro Queijos": 2},
	},
	"Lenon": PizzaPreferences{
		map[string]int{"Marguerita": 4, "Quatro Queijos": 5},
	},
	"Renata": PizzaPreferences{
		map[string]int{"Marguerita": 4, "Quatro Queijos": 5},
	},
	"Washington": PizzaPreferences{
		map[string]int{"Marguerita": 1, "Quatro Queijos": 1},
	},
	"Tino": PizzaPreferences{
		map[string]int{"Marguerita": 1, "Quatro Queijos": 5},
	},
	"Luca": PizzaPreferences{
		map[string]int{"Marguerita": 5, "Quatro Queijos": 4},
	},
}

func SharePizzaWith(person string, pizza string) []string {
	preferences := personPreferences[person].preferences
	grade := preferences[pizza]
	people := findPersonToShare(person, pizza, grade)
	return people
}

func findPersonToShare(person string, pizza string, minGrade int) []string {
	var results = make([]string, 0, len(personPreferences))

	for key, value := range personPreferences {
		if key != person && value.preferences[pizza] >= minGrade {
			results = append(results, key)
		}
	}
	return results
}
