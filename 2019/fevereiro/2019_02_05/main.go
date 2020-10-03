package dojo

import "strings"

func main(num int) string {
	var result []string
	numbers := map[int]string{
		1:  "I",
		5:  "V",
		10: "X",
	}
	nums, ok := numbers[num]
	if ok {
		result = append(result, nums)
		num = 0
	}
	for n := 1; n <= num; n++ {

		result = append(result, "I")
	}

	return strings.Join(result, "")

}
