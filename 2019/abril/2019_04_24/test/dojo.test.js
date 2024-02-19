var assert = require('assert');
var dojo = require('../src/dojo');


describe('Test True', function () {
    it('should push 1 return [1]', function () {
        let queue = new dojo()
        queue.push(1)
        assert.deepEqual(queue.getValue(), [1]);
    });
    it('should push 1 return [1]', function () {
        let queue = new dojo()
        queue.setValue([1])
        assert.deepEqual(queue.getValue(), [1]);
    });
    it('should push 2 return [2]', function () {
        let queue = new dojo()
        queue.push(2)
        assert.deepEqual(queue.getValue(), [2]);
    });
    it('should push 1,2 numbers and return [2, 1]', function () {
        let queue = new dojo()
        queue.push(1)
        queue.push(2)
        assert.deepEqual(queue.getValue(), [2,1]);
    });
    it('should push 1,2,3 numbers and return [3, 2,1]', function () {
        let queue = new dojo()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert.deepEqual(queue.getValue(), [3,2,1]);
    });
    it('should  return false if is not empty', function () {
        let queue = new dojo()
        queue.setValue([1,2,3,4])
        assert.deepEqual(queue.empty(), false);
    });
    it('should  return true if is empty', function () {
        let queue = new dojo()
        assert.deepEqual(queue.empty(), true);
    });
    it('should return the first element from array', function () {
        let queue = new dojo()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        let firstelement = queue.peek()
        assert.deepEqual(firstelement, 3);
    });
});

