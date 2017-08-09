package atm_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"testing"
)

func TestAtm(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Atm Suite")
}
