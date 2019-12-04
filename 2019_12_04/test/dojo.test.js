var assert = require('assert');
var {getLetter, getCombinations} = require('../src/dojo');


describe('Test True', function () {
  it('should return A when 1', function () {
        assert.equal(getLetter(1), 'A');
  });
  
  it('should return B when 2', function () {
        assert.equal(getLetter(2), 'B');
  });
  
  it('should return L when 12', function () {
        assert.equal(getLetter(12), 'L');
  });

  it('should return combination of 1 and 2 when 12', function () {
    assert.deepEqual(getCombinations("12"), [[1,2],[12]]);
  });

  it('should return combination of 1 and 3 when 13', function () {
    assert.deepEqual(getCombinations("13"), [[1,3],[13]]);
  });

  it('should return combination of 2 and 5 when 25', function () {
    assert.deepEqual(getCombinations("25"), [[2,5],[25]]);
  });
});
