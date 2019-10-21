package atm_test

import (
	. "github.com/globocom/dojo/2017_08_09/atm"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Atm", func() {
	Describe("saque no caixa eletronico", func() {
		Context("saque de R$ 30", func() {
			It("retorna uma nota de 20 e uma de 10", func() {
				result, err := Saque(30)
				Expect(result).To(BeEquivalentTo([]int{20, 10}))
				Expect(err).To(BeNil())
			})
		})

		Context("saque de R$ 80", func() {
			It("retorna uma nota de 50, uma de 20 e uma de 10", func() {
				result, err := Saque(80)
				Expect(result).To(BeEquivalentTo([]int{50, 20, 10}))
				Expect(err).To(BeNil())
			})
		})

		Context("saque de R$ 100", func() {
			It("retorna uma nota de 100", func() {
				result, err := Saque(100)
				Expect(result).To(BeEquivalentTo([]int{100}))
				Expect(err).To(BeNil())
			})
		})

		Context("saque de R$ 150", func() {
			It("retorna uma nota de 100, e uma de 50", func() {
				result, err := Saque(150)
				Expect(result).To(BeEquivalentTo([]int{100, 50}))
				Expect(err).To(BeNil())
			})
		})

		Context("saque de R$ 180", func() {
			It("retorna uma nota de 100, uma de 50, uma de 20, uma de 10", func() {
				result, err := Saque(180)
				Expect(result).To(BeEquivalentTo([]int{100, 50, 20, 10}))
				Expect(err).To(BeNil())
			})
		})

		Context("saque de R$ 240", func() {
			It("retorna duas notas de 100, e duas de 20", func() {
				result, err := Saque(240)
				Expect(result).To(BeEquivalentTo([]int{100, 100, 20, 20}))
				Expect(err).To(BeNil())
			})
		})

		Context("saque de R$ 15", func() {
			It("retorna erro", func() {
				_, err := Saque(15)
				Expect(err).To(Not(BeNil()))
			})
		})

		Context("saque de R$ -150", func() {
			It("retorna erro", func() {
				_, err := Saque(-150)
				Expect(err).To(Not(BeNil()))
			})
		})
	})
})
