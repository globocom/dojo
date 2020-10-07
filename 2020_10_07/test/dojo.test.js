var assert = require('assert');
var { transformWord, main } = require('../src/dojo');


describe('Test True', function () {
    it('should transform meef to 1|2|2|3', function () {
        assert.strictEqual(transformWord('meef'), '1|2|2|3');
    });

    it('should transform abc to 1|2|3', function () {
        assert.strictEqual(transformWord('abc'), '1|2|3');
    });

    it('should transform aaa to 1|1|1', function () {
        assert.strictEqual(transformWord('aaa'), '1|1|1');
    });

    it('should return list with match words 1', function () {
        assert.deepStrictEqual(main('aaa', ['bbb', 'abc']), ['bbb']);
    })

    it('should return list with match words 2', function () {
        assert.deepStrictEqual(main('xyz', ['aab', 'abc']), ['abc']);
    })

    it('should return list with match words 3', function () {
        assert.deepStrictEqual(main('xyy', ['abb', 'abc']), ['abb']);
    })

});

// Ingrid - Lucas - Mateus - Allan - Sami - Juan
//'meef' => '1|2|2|3'