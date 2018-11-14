package dojo

import "strings"

func wrap(phrase string, column int) string {
	wordList := strings.Split(phrase, " ")
	var line string
	count := 0
	for index, word := range wordList {
		count = len(line)
		if (len(line)-count+len(word))+1 > column {
			line += "\n" + word
			count = 0
		} else {
			if index > 0 {
				line += " "
			}
			line += word
		}
	}
	// if lenght > column {

	// 	result2 := strings.Join(result, "\n")
	// 	return result2
	// }

	return line
}
