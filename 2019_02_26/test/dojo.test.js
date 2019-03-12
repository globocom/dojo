var assert = require('assert');
var dojo = require('../src/dojo');


describe('Test True', function () {
    it('A should return A', function () {
        assert.deepEqual(dojo.matrix("A"), [["A"]]);
    });
    it('AB should return AB', function () {
        let ab = [
                     ["A"]
                ["B", " ", "B"]
            ]
        assert.deepEqual(dojo.matrix("AB"), ab);
    });
    it('Calc line must return letter in first position', function () {
        assert.deepEqual(dojo.calcInnerSpaces(1), 0);
    });
    it('Calc space must return in first position', function () {
        assert.deepEqual(dojo.calcInnerSpaces(2), 1);
    });

    it('Calc space must return in third position', function () {
        assert.deepEqual(dojo.calcInnerSpaces(3), 3);
    });

    it('Calc outer space must return first position', function () {
        assert.deepEqual(dojo.calcOuterSpace(1,3), 2);
    });

    it('Calc outer space must return second position', function () {
        assert.deepEqual(dojo.calcOuterSpace(2,3), 1);
    });

    it('Calc outer space must return third position', function () {
        assert.deepEqual(dojo.calcOuterSpace(3,3), 0);
    });
});
