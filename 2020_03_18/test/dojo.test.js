var assert = require('assert');
var arraySort = require('../src/dojo');


describe('Test True', function () {
    it('should return 1', function () {
        assert.deepEqual(arraySort([1]), [1]);
    });

    it('should return 1,2,3', function () {
        assert.deepEqual(arraySort([2,1,3]), [1,2,3]);
    });

    it('should return 1,2,3,5,6', function () {
        assert.deepEqual(arraySort([2,1,4,3,6,5]), [1,2,3,4,5,6]);
    });
});
