package dojo

func QuantityOfInterations(candies, prisoners int) int {
	return candies % prisoners
}

func GetBadLuckChair(prisoners, chairIndex, candies int) int {
	prisonersLeft := QuantityOfInterations(candies, prisoners)
	cursedChair := prisonersLeft + chairIndex - 1
	if cursedChair == 0 {
		return prisoners
	}
	return cursedChair
}
