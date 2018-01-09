package dojo_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"testing"
)

func TestDojo(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Dojo Suite")
}
