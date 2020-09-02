var assert = require("assert")
var { countdown } = require("../src/dojo")

describe("Test Countdon", function () {
  it("should return a count 1 for an array with one element", function () {
    assert.equal(countdown([1], 1), 1)
  })

  it("should return a count 1 for an array with one element", function () {
    assert.equal(countdown([2, 1, 3, 2, 1], 2), 2)
  })

  it("should return a count 1 for an array with one element", function () {
    assert.equal(countdown([], 3), 0)
  })

  it("should return a count 1 for an array with one element", function () {
    assert.equal(countdown([7, 3, 2], 4), 0)
  })

  //   it("should return a array without element 1", function () {
  //     assert.equal(countdown([2, 1, 3, 2, 2], 2), 1)
  //   })
})
