package main

import "sort"

func add(origin []string, values ...string) []string {
	for _, value := range values {
		count := 0
		for _, o := range origin {
			if value == o {
				break
			} else {
				count++
			}
		}
		if count == len(origin) {
			origin = append(origin, value)
		}
	}
	sort.Strings(origin)
	return origin
}

func dep(name string, input map[string][]string) []string {
	dependencies := []string{}
	for _, value := range input[name] {
		dependencies = add(dependencies, value)
		dependencies = add(dependencies, dep(value, input)...)
	}
	return dependencies
}

func Dependencies(input map[string][]string) map[string][]string {
	dependencies := map[string][]string{}

	for key, _ := range input {
		dependencies[key] = dep(key, input)
	}
	return dependencies
}
