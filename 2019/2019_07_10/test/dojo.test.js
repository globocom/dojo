var assert = require('assert');
var letterHole = require('../src/dojo').letterHole;
var sumLetterHole = require('../src/dojo').sumLetterHole;


describe('Test True', function () {
    it('A should be 1', function () {
        assert.equal(letterHole("A"), 1);
    });

    it('D should be 1', function () {
        assert.equal(letterHole("D"), 1);
    });

    it('O should be 1', function () {
        assert.equal(letterHole("O"), 1);
    });

    it('P should be 1', function () {
        assert.equal(letterHole("P"), 1);
    });

    it('Q should be 1', function () {
        assert.equal(letterHole("Q"), 1);
    });

    it('R should be 1', function () {
        assert.equal(letterHole("R"), 1);
    });

    it('B should be 2', function () {
        assert.equal(letterHole("B"), 2);
    });
    
    it('C should be 0', function () {
        assert.equal(letterHole("C"), 0);
    });

    it('AB should be 3', function () {
        assert.equal(sumLetterHole("AB"), 3);
    });

    it('BC should be 2', function () {
        assert.equal(sumLetterHole("BC"), 2);
    });

    it('ABCD should be 4', function () {
        assert.equal(sumLetterHole("ABCD"), 4);
    });

});
