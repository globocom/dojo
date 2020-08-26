var assert = require('assert');
var {previousNumbersAreSmaller, isLastDay, isLargerThanFollowing, main} = require('../src/dojo');


describe('Test True', function () {
    it('should return false if number is not the biggest till them', function () {
        assert.equal(previousNumbersAreSmaller([9,9,9,9,9], 1), false);
    });

    it('should return true if number is the biggest till them', function () {
        assert.equal(previousNumbersAreSmaller([1,2,0,7,2,0,2,0], 1), true);
    });

    it('should return false if number is not the biggest till them 2', function () {
        assert.equal(previousNumbersAreSmaller([1,2,0,7,2,0,2,0], 2), false);
    });

    it('should return false if number is not the last in array', function () {
        assert.equal(isLastDay([1,2,0,7,2,0,2,0], 4), false);
    });

    it('should return true if number is the last in array', function () {
        assert.equal(isLastDay([1,2,0,7,2,0,2,0], 7), true);
    });

    it('should return true if number is the last in array 2', function () {
        assert.equal(isLastDay([9,9,9,9], 3), true);
    });

    it('should return false if number is not bigger than following number', function () {
        assert.equal(isLargerThanFollowing([9,9,9,9], 3), false);
    });

    it('should return true if number is bigger than following number', function () {
        assert.equal(isLargerThanFollowing([9,9,9,11,10], 3), true);
    });

    it('should return false if number is not bigger than following number 2', function () {
        assert.equal(isLargerThanFollowing([9,9,9,10,11], 3), false);
    });

    it('should return the number of breakers', function () {
        assert.equal(main([1,2,0,7,2,0,2,0]), 2);
    });

    it('should return the number of breakers 2', function () {
        assert.equal(main([9,9,9,9,9,9]), 0);
    });

    it('should return the number of breakers 3', function () {
        assert.equal(main([3,1,4,1,5,9,2,6,5]), 3);
    });
});
