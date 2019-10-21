package cesar

func Cesar(str string, cifra int) string {
	result := ""
	for _, l := range str {
		tmp := int(l) + cifra
		if tmp > 'z' {
			tmp -= 26
		}
		result += string(rune(tmp))
	}
	return result
}
