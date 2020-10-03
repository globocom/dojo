var assert = require('assert');
var dojo = require('../src/dojo').dojo;
var checkRow = require('../src/dojo').checkRow;


describe('Test True', function () {
    it('[dad] should return [dad]', function () {
        assert.deepEqual(['dad'], dojo(['dad']));
    });

    it('[dad] should return [dad]', function () {
        assert.deepEqual(['dad'], dojo(['dad', 'hellow!']));
    });
    
    it('[dad, alaska] should return [dad, alaska]', function () {
        assert.deepEqual(['dad','alaska'], dojo(['dad', 'alaska']));
    });

    it('dad should return true', function () {
        assert.deepEqual(true, checkRow('dad',['a','d']));
    });
    
    it('dad should return false', function () {
        assert.deepEqual(false, checkRow('dad',['a','c']));
    });
    
    it('dad should return false again', function () {
        assert.deepEqual(false, checkRow('dad',['a','e']));
    });

    it('daD should return true again', function () {
        assert.deepEqual(true, checkRow('daD',['a','d']));
    });

    it('retiro should return true', function () {
        assert.deepEqual(['retiro'], dojo(['retiro']));
    });
    
    it('porto should return porto', function () {
        assert.deepEqual(['porto'], dojo(['porto']));
    });
    
    it('vc should return vc', function () {
        assert.deepEqual(['vc'], dojo(['vc']));
    });
    
    it('vc and tc should return vc', function () {
        assert.deepEqual(['vc'], dojo(['vc','tc']));
    });
    
});
