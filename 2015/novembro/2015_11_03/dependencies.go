package dependencies

import "sort"

func CalculateDeps(deps map[string][]string) map[string][]string {
	result := make(map[string][]string)
	for key, _ := range deps {
		acc := calculateInnerDeps(deps, key, make([]string, 0))
		if len(acc) > 0 {
			result[key] = acc
		}

	}
	return result
}

func calculateInnerDeps(deps map[string][]string, key string, acc []string) []string {
	dependencies := deps[key]
	for _, dependency := range dependencies {

		if !contains(acc, dependency) {
			acc = append(acc, dependency)
		}

		acc = calculateInnerDeps(deps, dependency, acc)
		sort.Strings(acc)

	}
	return acc
}

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}
