var assert = require('assert');
var {sum, verifySum, main} = require('../src/dojo');


describe('Test True', function () {
    it('should return sum of 2 and 3', function () {
        assert.equal(sum(2, 3), 5);
    });

    it('should return sum of 1 and 2', function () {
        assert.equal(sum(1, 2), 3);
    });

    it('should return sum of 5 and 6', function () {
        assert.equal(sum(5, 6), 11);
    });

    it('should return true if sum of 1 and 2 is 3', function () {
        assert.equal(verifySum(1, 2, 3), true);
    });

    it('should return false if sum of 2 and 3 is 6', function () {
        assert.equal(verifySum(2, 3, 6), false);
    });

    it('should return false if sum of 5 and 2 is 7', function () {
        assert.equal(verifySum(5, 2, 7), true);
    });

    it('should return 0 and 3', function (){
        assert.deepEqual(main([1,2,3,4], 5), [0,3])
    })

    it('should return 0 and 3', function (){
        assert.deepEqual(main([1,2,3,4], 3), [0,1])
    })

    it('should return 0 and 3', function (){
        assert.deepEqual(main([1,2,3,4], 7), [2,3])
    })

    it('should return 0 and 3', function (){
        assert.deepEqual(main([1,2,3,4], 10), [])
    })
});
