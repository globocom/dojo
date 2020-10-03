var assert = require('assert');
var {main, getCity} = require('../src/dojo');

describe('Test True', function () {
    it('should return destiny', function () {
        let cities = { "A": false, "B": true }
        assert.deepEqual(getCity([["A", "B"]]),cities);
    });

    it('should return destiny2', function () {
        let cities = { "A": false, "B": false, "C": true }
        assert.deepEqual(getCity([["A", "B"], ["B", "C"]]),cities );
    });

    it('should return destiny3', function () {
        let cities = { "A": false, "B": false, "C": false, "D": true }
        assert.deepEqual(getCity([["A", "B"], ["C", "D"],["B", "C"]]), cities );
    });

    it('should return main1', function () {
        assert.equal(main([["A", "B"], ["C", "D"],["B", "C"]]), "D");
    });

    it('should return main2', function () {
        assert.equal(main([["A", "B"]]), "B");
    });

    it('should return main3', function () {
        assert.equal(main([["A", "B"], ["B", "C"]]), "C");
    });
});
