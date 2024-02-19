package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestExtractProtocol(t *testing.T) {
	assert := assert.New(t)

	cases := []struct {
		input    string
		expected string
	}{
		{"http://www.google.com/mail?user=fulano", "http"},
		{"https://www.google.com/mail?user=fulano", "https"},
		{"ssh://www.google.com/mail?user=fulano", "ssh"},
	}
	for _, s := range cases {
		assert.Equal(extractProtocol(s.input), s.expected)
	}
}

func TestExtractHost(t *testing.T) {
	assert := assert.New(t)

	cases := []struct {
		input    string
		expected string
	}{
		{"http://www.google.com/mail?user=fulano", "www"},
		{"http://ww2.google.com/mail?user=fulano", "ww2"},
		{"http://ww4.google.com/mail?user=fulano", "ww4"},
	}
	for _, s := range cases {
		assert.Equal(extractHost(s.input), s.expected)
	}
}

func TestStripDomain(t *testing.T) {
	assert := assert.New(t)

	cases := []struct {
		input    string
		expected string
	}{
		{"www.google.com", "www.google"},
		{"www.google.com.br", "www.google"},
		{"www.com.google.com.br", "www.com.google"},
	}
	for _, s := range cases {
		assert.Equal(stripDomain(s.input), s.expected)
	}
}

// func TestExtractDominio(t *testing.T) {
// 	assert := assert.New(t)

// 	cases := []struct {
// 		input    string
// 		expected string
// 	}{
// 		{"http://www.google.com/mail?user=fulano", "google.com"},
// 		{"http://globo.com/mail?user=fulano", "globo.com"},
// 		{"http://ww4.voteeymael.com/mail?user=fulano", "ww4"},
// 	}
// 	for _, s := range cases {
// 		assert.Equal(extractHost(s.input), s.expected)
// 	}
// }
