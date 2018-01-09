package dojo

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Dojo", func() {
	Context("Test context description", func() {
		It("true must be true", func() {
			Expect(returnTrue()).To(Equal(true))
		})
	})
})
