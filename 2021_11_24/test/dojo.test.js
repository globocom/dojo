var assert = require('assert');
var createHashmap = require('../src/dojo');


describe('Test True', function () {
    it('should return the hashmap from array 1', function () {
        assert.deepEqual(createHashmap([1,1,1,2,2,3]), {1:3,2:2,3:1});
    });

    it('should return the hashmap from array 2', function () {
        assert.deepEqual(createHashmap([1]), {1:1});
    });

    it('should return the hashmap from array 3', function () {
        assert.deepEqual(createHashmap([1,1,2,2,2,3,3,3,4]), {1:2,2:3,3:3,4:1});
    });
});

// hashmap inicial = {}

// hashmap final = {1:3,2:2,3:1}
// results = [1,2]

// nums = [1,1,1,2,2,3], k = 2
// [1,2]

// nums = [1], k = 1
// [1]

// nums = [1,1,2,2,2,3,3,3,4] k = 3
// [2,3,1]

// Ingrid - Tiago - Alex - Christian - Cynthia
// hello world