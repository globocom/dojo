var assert = require("assert")
var dojo = require("../src/dojo")

describe("Test True", function() {
  it("() should return true", function() {
    assert.equal(dojo.main("()"), true)
  })

  it("( should return false", function() {
    assert.equal(dojo.main("("), false)
  })

  it("(()) should return true", function() {
    assert.equal(dojo.main("(())"), true)
  })

  it(")( should return false", function() {
    assert.equal(dojo.main(")("), false)
  })

  it("(123) should return true", function() {
    assert.equal(dojo.main("(123)"), true)
  })
})

describe("Test 2", function() {
  it("Test character (", function() {
    assert.equal(dojo.getScore("("), 1)
  })

  it("Test character [", function() {
    assert.equal(dojo.getScore("["), 1)
  })

  it("Test character )", function() {
    assert.equal(dojo.getScore(")"), -1)
  })

  it("Ignore characters 1", function() {
    assert.equal(dojo.getScore("1"), 0)
  })
  it("Ignore characters 2", function() {
    assert.equal(dojo.getScore("2"), 0)
  })
})

describe("Should evaluate []", function() {
  it("[] should return true", function() {
    assert.equal(dojo.main("[]"), true)
  })
  // it("][ should return false", function() {
  //   assert.equal(dojo.main("]["), false)
  // })
  it("[][] should return true", function() {
    assert.equal(dojo.main("[][]"), true)
  })
})
