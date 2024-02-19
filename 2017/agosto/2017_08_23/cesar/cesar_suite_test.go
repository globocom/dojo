package cesar_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"testing"
)

func TestCesar(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Cesar Suite")
}
