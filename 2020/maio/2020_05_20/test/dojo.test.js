var assert = require('assert');
var { convertLetter, main } = require('../src/dojo');

describe('ConverterLetra', function () {
    it('when receive A, should return 2', function () {
        assert.equal(convertLetter("A"), "2");
    });
    it('when receive B, should return 22', function () {
        assert.equal(convertLetter("B"), "22");
    });
    it('when receive C, should return 222', function () {
        assert.equal(convertLetter("C"), "222");
    });
    it('when receive space, should return _', function () {
        assert.equal(convertLetter(" "), "0");
    });
    it('when receive oi, should return 666444', function () {
        assert.equal(main("oi"), "666444");
    });
    it('when receive oi mundo, should return', function() {
        assert.equal(main("oi mundo"), "6664440688663666");
    })
    it('when receive sempre, should return', function() {
        assert.equal(main("sempre"), "77773367_77733");
    })
});




/*
ABC    ->  2
DEF    ->  3
GHI    ->  4
JKL    ->  5
MNO    ->  6
PQRS   ->  7
TUV    ->  8
WXYZ   ->  9
Espaço ->  0

77773367_77733

// 666444

'N' => '66'

Input: 'T este'
Output: '8_337777833'

Elen
Tiago
Juan
Sami
Natalia
Ingrid
Ícaro
Pedro
Allan
*/