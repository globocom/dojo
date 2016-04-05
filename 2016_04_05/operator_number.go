package main

func sum (x, y int) int { return x + y }
func diff (x, y int) int { return x - y }
func mult (x, y int) int { return x * y }

func NOS(value string) int {
	return_value := 0
	for i := 0; i < len(value); i++ {
		digit := string(value[i])
		j := i+1
		if digit == "0" {
			return_value = sum(return_value, j)
		} else if digit == "1" {
			return_value = diff(return_value, j)
		} else {
			return_value = mult(return_value, j)
		}
	}

	return return_value
}

func SON(value int) string {
	return "    "
}

func main() {

}
