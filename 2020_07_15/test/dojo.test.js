var assert = require("assert");
var { getValueToHash, incAscValue } = require("../src/dojo");

describe("Test True", function() {
  it("should return the ASCI numbers from a string", function() {
    assert.deepEqual(getValueToHash("ABC"), [65, 66, 67]);
  });

  it("should return the ASCI numbers from a string 2", function() {
    assert.deepEqual(getValueToHash("ABab"), [65, 66, 97, 98]);
  });

  it("should return the ASCI numbers from a string 3", function() {
    assert.deepEqual(getValueToHash("ABab123"), [65, 66, 97, 98, 49, 50, 51]);
  });

  it("should return the ASCI numbers plus 3", function() {
    assert.deepEqual(incAscValue([65, 66, 97, 98]), [68, 69, 100, 101]);
  });

  it("should return the ASCI numbers plus 3", function() {
    assert.deepEqual(incAscValue([65, 66, 97, 98, 49, 50, 51]), [
      68,
      69,
      100,
      101,
      49,
      50,
      51
    ]);
  });

  it("should return the ASCI numbers plus 4", function() {
    assert.deepEqual(incAscValue([50, 51]), [50, 51]);
  });
});
