var assert = require('assert');
var {getLetters, getMatrixSize} = require('../src/dojo');


describe('Test True', function () {
    it('should return A', function () {
            assert.deepEqual(getLetters('A'), ['A']);
    });

 it('should return A and B', function () {
        assert.deepEqual(getLetters('B'), ['A','B']);
    });

    it('should return A, B and C', function () {
        assert.deepEqual(getLetters('C'), ['A','B','C']);
    });

    it('should return matrix size', function () {
        assert.deepEqual(getMatrixSize('C'), 5);
    });

    it('should return matrix size', function () {
        assert.deepEqual(getMatrixSize('A'), 1);
    });

    it('should return matrix size', function () {
        assert.deepEqual(getMatrixSize('B'), 3);
    });

});
