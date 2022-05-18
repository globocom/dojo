package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// An ABBA is any four-character sequence which consists
// of a pair of two different characters followed by the reverse of that pair

// the IP also must not have an ABBA within any hypernet sequences,
// which are contained by square brackets

func TestMain(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main(), true, "must be true")
}

func TestIsABBA(t *testing.T) {
	assert := assert.New(t)
	assert.False(IsABBA("abcd"))
	assert.False(IsABBA("aaaa"))
	assert.True(IsABBA("abba"))
	assert.True(IsABBA("oxxo"))
}
func TestHasABBA(t *testing.T) {
	assert := assert.New(t)
	assert.False(HasABBA("abcdef"))
	assert.True(HasABBA("abbaef"))
	assert.True(HasABBA("xaabbaf"))
	assert.True(HasABBA("xasdfdkwhjgejduiiu"))
}

func TestParseLine(t *testing.T) {
	assert := assert.New(t)
	var r1, r2 []string

	r1, r2 = ParseLine("abba[xxss]")
	assert.Equal([]string{"abba"}, r1)
	assert.Equal([]string{"xxss"}, r2)

	r1, r2 = ParseLine("abba[xxss]pooo")
	assert.Equal([]string{"abba", "pooo"}, r1)
	assert.Equal([]string{"xxss"}, r2)

	r1, r2 = ParseLine("abba[xxss]pooo[cenasdois]maisoutro")
	assert.Equal(r1, []string{"abba", "pooo", "maisoutro"})
	assert.Equal(r2, []string{"xxss", "cenasdois"})

	r1, r2 = ParseLine("abba")
	assert.Equal(r1, []string{"abba"})
	assert.Equal(r2, []string{})
}

func TestCountLine(t *testing.T) {
	assert := assert.New(t)

	assert.Equal(0, CountLine("abba[poop]"))
	assert.Equal(1, CountLine("abba[xxss]pooo"))
	assert.Equal(0, CountLine("acba[xxss]pooo[cenasdois]maisoutro"))
	assert.Equal(1, CountLine("abba"))
}

func TestPart1(t *testing.T) {
	assert.Equal(t, 110, Part1(ProblemInput))
}

// - separar cada linha
// - parseLine() -> [insideBrackets], [outsideBrackets]
//			- forEach insideBrackets
//				- se hasABBA() -> return false
//			- forEach outsideBrackets
//				- se hasABBA() -> return true
//			- else false

// - hasABBA() { ... isABBA("abcd") ... }
// -> s = abcdefghij
//			for 0 .. Len(s)-4
// 				isABBA(s[i:i+4]) -> ( s[0] == s[3] && s[1] == s[2] && s[0] != s[1] )
//

// examples:
// abba[mnop]qrst supports TLS (abba outside square brackets).
// abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
// aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
// ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
