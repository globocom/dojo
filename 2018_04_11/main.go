package main

func Spatula(pancakes *[]int, position int) {
	// var result = make([]int, len(*pancakes))
	p := *pancakes
	start := position
	end := len(p) - 1
	for {
		p[start], p[end] = p[end], p[start]
		start++
		end--
		if start >= end {
			break
		}
	}
}
