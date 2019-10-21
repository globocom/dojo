var assert = require("assert")
var interval = require("../src/dojo")

describe("Intervals", function() {
  it("should return one value when passing one value", function() {
    assert.deepEqual(interval(1), [1])
  })

  it("should return one value when passing one value", function() {
    assert.deepEqual(interval(1, 2), [1, 2])
  })
  it("should return two value when passing three value", function() {
    assert.deepEqual(interval(1, 2, 3), [1, 3])
  })
  it("should return two value when passing three value", function() {
    assert.deepEqual(interval(1, 2, 4), [1, 2])
  })
})
