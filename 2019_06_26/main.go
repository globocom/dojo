package dojo

func main(dependencies [][]string, value string) []string {
	for _, dep := range dependencies {
		if dep[0] == value {
			return dep[1:]
		}
	}
	return []string{}
}
