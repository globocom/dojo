package cesar_test

import (
	"github.com/globocom/dojo/2017_08_23/cesar"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Cesar", func() {
	Context("criptografar com a cifra 3", func() {
		It("retorna d quando informado a", func() {
			Expect(cesar.Cesar("a", 3)).To(Equal("d"))
		})

		It("retorna e quando informado b", func() {
			Expect(cesar.Cesar("b", 3)).To(Equal("e"))
		})

		It("retorna c quando informado z", func() {
			Expect(cesar.Cesar("z", 3)).To(Equal("c"))
		})

		It("retorna b quando informado y", func() {
			Expect(cesar.Cesar("y", 3)).To(Equal("b"))
		})

		It("retorna a quando informado x", func() {
			Expect(cesar.Cesar("x", 3)).To(Equal("a"))
		})

		It("retorna de quando informado ab", func() {
			Expect(cesar.Cesar("ab", 3)).To(Equal("de"))
		})

		It("retorna fd quando informado ca", func() {
			Expect(cesar.Cesar("ca", 3)).To(Equal("fd"))
		})

		It("retorna o alfabeto cifrado", func() {
			Expect(cesar.Cesar("abcdefghijklmnopqrstuvwxyz", 3)).To(Equal("defghijklmnopqrstuvwxyzabc"))
		})
	})

})
