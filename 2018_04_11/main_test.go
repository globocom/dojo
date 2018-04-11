package main_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	. "github.com/globocom/dojo/2018_04_11"
)

var _ = Describe("Pancake sorter", func() {
	Context("Spatula", func() {
		It("flips everything with 3 pancakes", func() {
			pancakes := []int{1, 2, 3}
			Spatula(&pancakes, 0)
			Expect(pancakes).To(Equal([]int{3, 2, 1}))
		})
		It("flips everything with 4 pancakes above position 0", func() {
			pancakes := []int{1, 2, 3, 4}
			Spatula(&pancakes, 0)
			Expect(pancakes).To(Equal([]int{4, 3, 2, 1}))
		})
		It("flips everything with 4 pancakes above position 1", func() {
			pancakes := []int{1, 2, 3, 4}
			Spatula(&pancakes, 1)
			Expect(pancakes).To(Equal([]int{1, 4, 3, 2}))
		})
		It("flips everything with 6 pancakes above position 2", func() {
			pancakes := []int{1, 3, 5, 2, 4, 6}
			Spatula(&pancakes, 2)
			Expect(pancakes).To(Equal([]int{1, 3, 6, 4, 2, 5}))
		})

		It("flips everything with 6 pancakes above position 5", func() {
			pancakes := []int{1, 3, 5, 2, 4, 6}
			Spatula(&pancakes, 5)
			Expect(pancakes).To(Equal([]int{1, 3, 5, 2, 4, 6}))
		})

		It("flips everything with 5 pancakes above position 4", func() {
			pancakes := []int{1, 3, 5, 2, 4}
			Spatula(&pancakes, 4)
			Expect(pancakes).To(Equal([]int{1, 3, 5, 2, 4}))
		})
	})
})
