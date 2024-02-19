package main

import (
	"math"
)

type person struct {
	x float64
	y float64
}

type distances struct {
	distance float64
	person   person
}

func distance(p1, p2 person) float64 {
	dx := math.Pow((p2.x - p1.x), 2)
	dy := math.Pow((p2.y - p1.y), 2)
	return math.Sqrt(dx + dy)
}

func (s person) closer(people []person) []person {
	var menorDist *distances
	for _, p := range people {
		d := distance(s, p)
		if (menorDist == nil) || (menorDist.distance > d) {
			menorDist = &distances{
				distance: d,
				person:   p,
			}
		}
	}
	return []person{menorDist.person}
}
