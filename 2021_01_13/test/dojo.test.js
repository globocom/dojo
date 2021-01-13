var assert = require('assert');
var {getContainersLength, sortList} = require('../src/dojo');


describe('Test True', function () {
 it('should return numbers of containers equal 3', function () {
        assert.strictEqual(getContainersLength([16, 18, 10, 13, 2, 9, 17, 17, 0, 19]), 3);
    });
 it('should return numbers of containers equal 4', function () {
        assert.strictEqual(getContainersLength([1, 2, 3, 21, 7, 12, 14, 21]), 4);
    });
 it('should return numbers of containers equal 2', function () {
        assert.strictEqual(getContainersLength([1, 2, 3, 4, 5, 10, 11, 12, 13]), 2);
    });
 it('should return a sorted list 1', function () {
        assert.deepStrictEqual(sortList([1, 2, 5, 4, 10]), [1, 2, 4, 5, 10]);
    });
 it('should return a sorted list 2', function () {
     assert.deepStrictEqual(sortList([1, 5, 2]), [1, 2, 5]);
 });
 it('should return a sorted list 3', function () {
    assert.deepStrictEqual(sortList([1,11, 10, 2]), [1, 2, 10, 11]);
});
});


