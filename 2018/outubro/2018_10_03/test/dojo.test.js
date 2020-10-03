import { expect } from "chai"

import { main } from "../src/dojo"

describe("dojo", () => {
  it("should passs: 2 - 3 \\o/", () => {
    expect(main(2, 3)).to.be.deep.equal([[0, 0], [1, 1], [2, 2]])
  })

  it("should pass 3 - 4", () => {
    expect(main(3, 4)).to.be.deep.equal([[0, 0], [1, 1], [2, 2], [3, 3]])
  })

  it("should pass 3 - 3", () => {
    expect(main(3, 3)).to.be.deep.equal([[0, 0], [1, 2], [3, 3]])
  })
  it(" should pass with 10 - 3", () => {
    expect(main(10, 3)).to.be.deep.equal([[0, 0], [1, 9], [10, 10]])
  })
  it(" should pass with 10 - 5", () => {
    expect(main(10, 5)).to.be.deep.equal([
      [0, 0],
      [1, 3],
      [4, 6],
      [7, 9],
      [10, 10],
    ])
  })
  it(" should pass with 21 - 4", () => {
    expect(main(21, 4)).to.be.deep.equal([[0, 0], [1, 10], [11, 20], [21, 21]])
  })
})
