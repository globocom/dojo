package main_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/globocom/dojo/2018_05_09"
)

var _ = Describe("Dependencies", func() {
	Context("Test", func() {
		It("one dependency", func() {
			input := map[string][]string{
				"A": []string{"B"},
			}
			Expect(Dependencies(input)).To(Equal(input))
		})

		It("two dependencies", func() {
			input := map[string][]string{
				"A": []string{"B"},
				"B": []string{"C"},
			}
			output := map[string][]string{
				"A": []string{"B", "C"},
				"B": []string{"C"},
			}
			Expect(Dependencies(input)).To(Equal(output))
		})

		It("three dependencies", func() {
			input := map[string][]string{
				"A": []string{"B"},
				"B": []string{"C"},
				"C": []string{"D"},
			}
			output := map[string][]string{
				"A": []string{"B", "C", "D"},
				"B": []string{"C", "D"},
				"C": []string{"D"},
			}
			Expect(Dependencies(input)).To(Equal(output))
		})

		It("all dependencies", func() {
			input := map[string][]string{
				"A": []string{"B", "C"},
				"B": []string{"C", "E"},
				"C": []string{"G"},
				"D": []string{"A", "F"},
				"E": []string{"F"},
				"F": []string{"H"},
			}

			output := map[string][]string{
				"A": []string{"B", "C", "E", "F", "G", "H"},
				"B": []string{"C", "E", "F", "G", "H"},
				"C": []string{"G"},
				"D": []string{"A", "B", "C", "E", "F", "G", "H"},
				"E": []string{"F", "H"},
				"F": []string{"H"},
			}
			Expect(Dependencies(input)).To(Equal(output))
		})

		/*It("circular dependencies", func() {
			input := map[string][]string{
				"A": []string{"B"},
				"B": []string{"C"},
				"C": []string{"A"},
			}
			Expect(Dependencies(input)).To(Panic())
		})*/
	})
})
