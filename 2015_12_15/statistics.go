package statistics

import "sort"

type Statistics struct {
	Max         int
	Min         int
	NumElements int
	Mean        int
}

func GetStatistics(values []int) (statistics Statistics) {
	sort.Ints(values)
	statistics.Max = values[len(values)-1]
	statistics.Min = values[0]
	statistics.NumElements = len(values)
	statistics.Mean = calculateMean(values)
	return
}

func calculateMean(values []int) int {
	var sum int
	for _, v := range values {
		sum += v
	}
	return sum / len(values)
}
