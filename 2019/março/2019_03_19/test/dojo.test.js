var assert = require('assert');
var dojo = require('../src/dojo').main;
var intermediate = require('../src/dojo').intermediate;

describe('Test True', function () {
    it('[1] with target 1 should return [[1]]', function () {
        assert.deepEqual(dojo([1], 1), [[1]]);
    });

    it('[1] with target 2 should return [[1, 1]]', function () {
        assert.deepEqual(dojo([1], 2), [[1, 1]]);
    });
    it('[1] with target 3 should return [[1, 1, 1]]', function () {
        assert.deepEqual(dojo([1], 3), [[1, 1 ,1]]);
    });

    it('[2] with target 2 should return [[2]]', function () {
        assert.deepEqual(dojo([2], 2), [[2]]);
    });

    it('[3] with target 3 should return [[3]]', function () {
        assert.deepEqual(dojo([3], 3), [[3]]);
    });

    it('[1, 2] with target 2 should return [[1, 1], [2]]', function () {
        assert.deepEqual(dojo([1, 2], 2), [[1, 1], [2]]);
    });

    it('[2] with target 1 should return []', function () {
        assert.deepEqual(dojo([2], 1), []);
    });

    it('[1, 2, 3] with target 3 should return [[1, 1, 1], [1, 2], [3]]', function () {
        assert.deepEqual(dojo([1, 2, 3], 3), [[1, 1, 1], [1, 2], [3]]);
    });
});

describe("intermediate", function() {
    xit("", function() {
        assert.deepEqual(intermediate([1, 2, 3], 3), [1, 2]);        
    })
})

