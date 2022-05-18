package dojo

import (
	"regexp"
	"strings"
)

func main() bool {
	return true
}

func IsABBA(s string) bool {
	return s[0] == s[3] && s[1] == s[2] && s[0] != s[1]
}

func HasABBA(s string) bool {
	for i := 0; i <= len(s)-4; i++ {
		subStr := s[i : i+4]
		if IsABBA(subStr) {
			return true
		}
	}
	return false

}

func ParseLine(s string) (outsideBrackets, insideBrackets []string) {
	re := regexp.MustCompile(`\[.*?\]`)
	submatchall := re.FindAllStringIndex(s, -1)

	// inside
	for _, irange := range submatchall {
		insideBrackets = append(insideBrackets, s[irange[0]+1:irange[1]-1])
	}

	// outside
	if len(submatchall) == 0 {
		insideBrackets = []string{}
		outsideBrackets = []string{s}
		return
	}
	outsideBrackets = append(outsideBrackets, s[0:submatchall[0][0]])
	for i := 0; i < len(submatchall)-1; i++ {
		curr := submatchall[i]
		next := submatchall[i+1]
		outsideBrackets = append(outsideBrackets, s[curr[1]:next[0]])
	}
	if s[len(s)-1] != ']' {
		l := len(submatchall) - 1
		outsideBrackets = append(outsideBrackets, s[submatchall[l][1]:])
	}
	return
}

func CountLine(line string) int {
	outsiders, insiders := ParseLine(line)
	for _, insider := range insiders {
		if HasABBA(insider) {
			return 0
		}
	}
	for _, outsider := range outsiders {
		if HasABBA(outsider) {
			return 1
		}
	}
	return 0
}

func Part1(input string) int {
	counter := 0
	for _, line := range strings.Split(input, "\n") {
		counter += CountLine(line)
	}
	return counter
}
