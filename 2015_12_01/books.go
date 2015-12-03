package books

func Price(books []int) float64 {
	price := 8.0

	booksMap := buildBooksPriceMap(books)

	amount := 0.0

	for {
		differentBooks := len(booksMap)

		if differentBooks == 0 {
			return amount
		}
		discount := getDiscount(differentBooks)
		amount += float64(differentBooks) * price * (1 - discount)

		for key := range booksMap {
			booksMap[key]--
			if booksMap[key] == 0 {
				delete(booksMap, key)
			}
		}
	}
}

func getDiscount(qty int) float64 {
	switch qty {
	case 2:
		return 0.05
	case 3:
		return 0.1
	case 4:
		return 0.2
	case 5:
		return 0.25
	default:
		return 0.0
	}
}

func buildBooksPriceMap(books []int) map[int]int {
	booksMap := make(map[int]int)

	for i := 0; i < len(books); i++ {
		bookIndex := books[i]
		_, exists := booksMap[bookIndex]
		if !exists {
			booksMap[bookIndex] = 1
		} else {
			booksMap[bookIndex]++
		}
	}

	return booksMap
}
