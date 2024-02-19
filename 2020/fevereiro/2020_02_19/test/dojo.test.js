var assert = require("assert");
var { stepToReduce, isOddNumber, calcNumber } = require("../src/dojo");

describe("Test True", function() {
  it("should return true", function() {
    assert.equal(stepToReduce(8), 4);
  });

  it("should return true", function() {
    assert.equal(stepToReduce(2), 2);
  });

  it("should return true", function() {
    assert.equal(stepToReduce(4), 3);
  });

  it("should return true", function() {
    assert.equal(stepToReduce(5), 4);
  });
});

describe("isOddNumber", function() {
  it("returns true with odd number", function() {
    assert.equal(isOddNumber(5), true);
  });

  it("returns false with even number", function() {
    assert.equal(isOddNumber(4), false);
  });
});

describe("calcNumber", function() {
  it("returns next number", function() {
    assert.equal(calcNumber(5), 4);
  });

  it("returns next number", function() {
    assert.equal(calcNumber(4), 2);
  });

  it("returns next number", function() {
    assert.equal(calcNumber(18), 9);
  });
});
