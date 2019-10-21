var assert = require("assert")
var dojo = require("../src/dojo").main
var getStartIndex = require("../src/dojo").getStartIndex
var getEndIndex = require("../src/dojo").getEndIndex
var extract = require("../src/dojo").extract
var decrypt = require("../src/dojo").decrypt
var decryptRecursive = require("../src/dojo").decryptRecursive

describe("Test True", function() {
  it("should return a", function() {
    assert.equal(dojo("a"), "a")
  })

  it("should return ab", function() {
    assert.equal(dojo("ab"), "ab")
  })

  it("getStartIndex should return the index of first `[`", function() {
    assert.equal(getStartIndex("1[c]"), 1)
  })

  it("getStartIndex should return the index of first `[` 2", function() {
    assert.equal(getStartIndex("a1[c]"), 2)
  })

  it("getEndIndex should return the index of first `]`", function() {
    assert.equal(getEndIndex("1[c]"), 3)
  })

  it("getEndIndex should return the index of last `]`", function() {
    assert.equal(getEndIndex("12[c]"), 4)
  })

  it("extract text inside `[]`", function() {
    assert.equal(extract(0, 2, "[c]"), "c")
  })

  it("decrypt text inside `[]`", function() {
    assert.equal(decrypt("2[c]"), "cc")
  })

  it("decrypt text inside `[]`", function() {
    assert.equal(decrypt("3[a]"), "aaa")
  })

  it("decrypt text inside repeat 6 `[]`", function() {
    assert.equal(decrypt("6[x]"), "xxxxxx")
  })

  it("decrypt text inside `[]`", function() {
    assert.equal(decrypt("2[ab]"), "abab")
  })

  it("decrypt text inside recursive `[]`", function() {
    assert.equal(decryptRecursive("2[3[a]b]"), "aaabaaab")
  })

  it("decrypt text inside recursive `[]`", function() {
    assert.equal(decryptRecursive("3[2[a]b]"), "aabaabaab")
  })
})
