var assert = require("assert");
var { toDecimal, palindromo } = require("../src/dojo");

describe("Test True", function () {
  it("should return 1", function () {
    assert.equal(toDecimal("1"), 1);
  });
  it("should return 10", function () {
    assert.equal(toDecimal("A"), 10);
  });
  it("should return 15", function () {
    assert.equal(toDecimal("F"), 15);
  });
  it("should return 25", function () {
    assert.equal(toDecimal("19"), 25);
  });
  it("should return true", function () {
    assert.equal(palindromo(101), true);
  });
  it("should return false", function () {
    assert.equal(palindromo(19), false);
  });
  it("should return true", function () {
    assert.equal(palindromo(123321), true);
  });
});

