var assert = require("assert");
var { dojo, inverte, extra, main } = require("../src/dojo");

describe("Dojo", function() {
  it("should return d", function() {
    assert.equal(dojo("a"), "d");
  });
  it("should return dddfg", function() {
    assert.equal(dojo("aaacd"), "dddfg");
  });
  it("should return 4", function() {
    assert.equal(dojo("4"), "4");
  });
  it("invert character a", function() {
    assert.equal(inverte("a"), "a");
  });
  it("invert character cde", function() {
    assert.equal(inverte("cde"), "edc");
  });
  it("invert character abcdefghijklmnopqrsuvwwxyz", function() {
    assert.equal(
      inverte("abcdefghijklmnopqrsuvwwxyz"),
      "zyxwwvusrqponmlkjihgfedcba"
    );
  });
  it("extra ab - > aa", function() {
    assert.equal(extra("ab"), "aa");
  });
  it("extra bbb - > baa", function() {
    assert.equal(extra("bbb"), "baa");
  });
  it("extra ccbbbc - > ccbaab", function() {
    assert.equal(extra("ccbbbc"), "ccbaab");
  });
  it("extra 3# rvzgV - > ccbaab", function() {
    assert.equal(main("Texto #3"), "3# rvzgV");
  });
  it("extra 3# abcABC1 - > 1FECedc", function() {
    assert.equal(main("abcABC1"), "1FECedc");
  });
  it("extra 3# vv.xwfxo.fd - > gi.r{hyz-xx", function() {
    assert.equal(main("vv.xwfxo.fd"), "gi.r{hyz-xx");
  });
});
