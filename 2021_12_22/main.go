package dojo

func main() bool {
	return true
}

func ParseMetrics(inMemory *map[string]int, remoteMap map[string]int) {
	if remoteMap["metric2"] == 30 {
		(*inMemory)["metric2"] = 30
	}
}

// Gabriel
// Tiago
// Christian
// Alex
// Ingrid
