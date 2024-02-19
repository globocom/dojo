package dojo

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPointIn(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(true, main(), "must be true")
	assert.Equal("http", protocolo("http://www.globo.com"), "must return http")
	assert.Equal("https", protocolo("https://www.globo.com"), "must return https")
	assert.Equal("ftp", protocolo("ftp://www.globo.com"), "must return https")

	assert.Equal("globo.com", dominio("https://www.globo.com"))
	assert.Equal("google.com", dominio("https://www.google.com"))
	assert.Equal("globo.com", dominio("https://www.g1.globo.com"))

	assert.Equal("www", subdominio("https://www.globo.com"))
	assert.Equal("g1", subdominio("https://g1.globo.com"))
	assert.Equal(nil, subdominio("https://globo.com"))
	assert.Equal("g1.qa", sub2("https://g1.qa.globo.com"))

}
