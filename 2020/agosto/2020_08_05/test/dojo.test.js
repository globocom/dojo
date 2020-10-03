var assert = require('assert');
var countBreaks = require('../src/dojo');


describe('Test True', function () {
    it('should return the numbers of breaks 1', function () {
        assert.equal(countBreaks([1, 2], 'A'), 0);
    });

    it('should return the numbers of breaks 2', function () {
        assert.equal(countBreaks([1, 2], 'D'), 1);
    });

    it('should return the numbers of breaks 3', function () {
        assert.equal(countBreaks([3, 1, 2, 3, 7, 5], 'C'), 2);
    });
})

// Sami - Ingrid - Tiago - Elen - Juan - Natalia - Mateus
