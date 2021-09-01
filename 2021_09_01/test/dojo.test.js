var assert = require('assert');
var { main, MyHashMap } = require('../src/dojo');


describe('Test True', function () {
    it('should return true', function () {
        assert.equal(main(), true);
    });
});
