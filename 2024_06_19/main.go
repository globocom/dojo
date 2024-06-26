package main

import "fmt"

type Mapa [][]string

func main() {
	mapa := Mapa{
		{" ", " ", "N", " ", " ", " ", "N", "N"},
		{" ", "N", "N", " ", " ", " ", " ", " "},
		{"N", "N", "N", " ", " ", " ", " ", " "},
		{" ", "N", " ", " ", " ", " ", " ", " "},
		{" ", "N", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " ", "A"},
	}

	atingiuAeroporto := false
	dias := 1
	for !atingiuAeroporto {
		dias++
		atingiuAeroporto = incrementarDias(mapa)
	}
	fmt.Println("Dias para atingir o aeroporto:", dias)
}

func incrementarDias(mapa Mapa) bool {
	for l, linha := range mapa {
		for c := range linha {
			if mapa[l][c] == " " || mapa[l][c] == "A" {
				continue
			}

			if mapa[l][c] == "n" {
				mapa[l][c] = "N"
				continue
			}

			if c > 0 {
				if mapa[l][c-1] == "A" {
					return true
				}
				mapa[l][c-1] = "N"
			}
			if c < len(linha)-1 && mapa[l][c+1] != "N" {
				if mapa[l][c+1] == "A" {
					return true
				}
				mapa[l][c+1] = "n"
			}
			if l > 0 {
				if mapa[l-1][c] == "A" {
					return true
				}
				mapa[l-1][c] = "N"
			}
			if l < len(mapa)-1 && mapa[l+1][c] != "N" {
				if mapa[l+1][c] == "A" {
					return true
				}
				mapa[l+1][c] = "n"
			}
		}
	}

	imprimirMapa(mapa)
	return false
}

func imprimirMapa(mapa Mapa) {
	for _, linha := range mapa {
		fmt.Println(linha)
	}
	fmt.Println()
}
