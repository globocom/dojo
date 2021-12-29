package dojo

func main() bool {
	return true
}

func ParseMetrics(inMemory *map[string]int, remoteMap map[string]int) {
	// O(n)
	for k, v := range remoteMap {
		if (*inMemory)[k] != v {
			(*inMemory)[k] = v
		}
	}

	// O(n)
	for k := range *inMemory {
		if _, ok := remoteMap[k]; !ok {
			delete((*inMemory), k)
		}
	}
}
