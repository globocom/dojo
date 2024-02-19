package dojo


func matchString(input string, exp string) bool {
	if input[0] == '*'{
		return false
	}
	pointer := 0
	for i := 0; i<len(input); i++{
		if input[i] != exp[pointer] && exp[pointer] != '.'{
			return false
		}
		if exp[pointer + 1] != '*'{
			pointer++
		}
	}
	return true
}
