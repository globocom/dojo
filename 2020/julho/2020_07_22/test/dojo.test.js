var assert = require("assert");
var {
  getValueToHash,
  incAscValue,
  codeReverse,
  shiftFromMiddleToEnd,
  convertAsciiToString,
  isASCIILetter,
  main
} = require("../src/dojo");

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

  it("should return the reverse code numbers 1", function() {
    assert.deepEqual(codeReverse([50, 51]), [51, 50]);
  });

  it("should return the reverse code numbers 2", function() {
    assert.deepEqual(codeReverse([50, 51, 80]), [80, 51, 50]);
  });

  it("should return the reverse code numbers 3", function() {
    assert.deepEqual(codeReverse([]), []);
  });

  it("should return the third step from passed string", function() {
    assert.deepEqual(shiftFromMiddleToEnd([50, 51, 52]), [50, 50, 51]);
  });

  it("should return the third step from passed string 2", function() {
    assert.deepEqual(shiftFromMiddleToEnd([51, 53, 54]), [51, 52, 53]);
  });

  it("should return the third step from passed string 3", function() {
    assert.deepEqual(shiftFromMiddleToEnd([80, 49, 98, 23]), [80, 49, 97, 22]);
  });

  it("should return decoded ascii string from numbers", function() {
    assert.deepEqual(convertAsciiToString([65, 66, 67]), "ABC");
  });

  it("should return decoded ascii string from numbers 2", function() {
    assert.deepEqual(convertAsciiToString([65, 66, 97, 98]), "ABab");
  });

  it("should return decoded ascii string from numbers 3", function() {
    assert.deepEqual(
      convertAsciiToString([65, 66, 97, 98, 49, 50, 51]),
      "ABab123"
    );
  });

  it("should return encrypted number", function() {
    assert.equal(main("Texto #3"), "3# rvzgV");
  });

  it("should return encrypted number 2", function() {
    assert.equal(main("abcABC1"), "1FECedc");
  });

  it("should return encrypted number 3", function() {
    assert.equal(main("vv.xwfxo.fd"), "gi.r{hyz-xx");
  });

  it("should return true for ascii letters", function() {
    assert.equal(isASCIILetter(65), true);
  });

  it("should return true for ascii letters", function() {
    assert.equal(isASCIILetter(101), true);
  });

  it("should return true for ascii letters", function() {
    assert.equal(isASCIILetter(30), false);
  });
});
