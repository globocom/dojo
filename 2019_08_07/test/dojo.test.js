var assert = require('assert');
var dojo = require('../src/dojo');


describe('Test True', function () {
    it('should return true', function () {
        assert.deepEqual(dojo(1, 1), ['*']);
        
    });

    it('should return true 2', function () {
        assert.deepEqual(dojo(2, 1), [' ','*']);
    });

    it('should return true 3', function () {
        assert.deepEqual(dojo(3, 2), [' ','*','*']);
    });
});
