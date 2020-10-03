var assert = require("assert");
var { sortArray, checkDifference, biggestArray } = require("../src/dojo");

describe("Test True", function() {
  it("should sort array", function() {
    assert.deepEqual(sortArray([5, 4, 2, 1, 1, 2]), [1, 1, 2, 2, 4, 5]);
  });

  it("should sort array 2", function() {
    assert.deepEqual(sortArray([3, 2, 1, 1, 2, 3]), [1, 1, 2, 2, 3, 3]);
  });

  it("should sort array 3", function() {
    assert.deepEqual(sortArray([4, 3, 2]), [2, 3, 4]);
  });

  it("should verify if difference is smaller than one", function() {
    assert.equal(checkDifference(2, 1), true);
  });

  it("should verify if difference is smaller than one 2", function() {
    assert.equal(checkDifference(7, 1), false);
  });
  it("should verify if difference is smaller than one 3", function() {
    assert.equal(checkDifference(9, 1), false);
  });
  it("should verify if difference is smaller than one 4", function() {
    assert.equal(checkDifference(1, 9), false);
  });
  it("should return the number of elements of the biggest array ", function() {
    assert.equal(biggestArray([[1, 1, 2, 2, 3], [1, 1, 2, 2, 3, 3, 4]]), 7);
  });

  it("should return the number of elements of the biggest array 1", function() {
    assert.equal(biggestArray([[1, 1, 2, 2, 3], [1, 1, 2, 2, 3, 3, 8, 9]]), 8);
  });

  it("should return the number of elements of the biggest array 2", function() {
    assert.equal(biggestArray([[1, 1, 2, 2, 3], [1, 1, 2, 2, 3, 3, 8, 9, 10]]), 9);
  });

  it("should return the number of elements of the biggest array 3", function() {
    assert.equal(biggestArray([[1, 1, 2, 2, 3], [1, 1, 2, 2], [1, 2, 3, 4]]), 5);
  });

  it("should return the number of elements of the biggest array 3", function() {
    assert.equal(biggestArray([[1, 1, 2, 2, 3], [1, 1, 2, 2], [1, 2, 3, 4]]), 5);
  });
});
