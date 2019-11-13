var assert = require('assert');
var RedKnight = require('../src/dojo');

describe('Test True', function () {
    it('should return final position', function () {
        const redKnight = new RedKnight(1,2)
        assert.deepEqual(redKnight.getPosition(), [1,2] )
    });

    it('should return final position2', function () {
        const redKnight = new RedKnight(3,4)

        assert.deepEqual(redKnight.getPosition(), [3,4] )
    });

    it('should return final position4', function () {
        const redKnight = new RedKnight(5,6)

        assert.deepEqual(redKnight.getPosition(), [5,6] )
    });

    it('should return final position5', function () {
        const redKnight = new RedKnight()

        assert.deepEqual(redKnight.getPosition(), [0,0] )
    });

    it('should return final position', function () {
        const redKnight = new RedKnight(0,0)
        redKnight.moveLR()
        assert.deepEqual(redKnight.getPosition(), [1,2] )
    });

    it('should return final position', function () {
        const redKnight = new RedKnight(1,0)
        redKnight.moveLL()
        assert.deepEqual(redKnight.getPosition(), [0,2] )
    });

    it('should return final position', function () {
        const redKnight = new RedKnight(2,0)
        redKnight.moveL()
        assert.deepEqual(redKnight.getPosition(), [0,0] )
    });

    it('should return final position', function () {
        const redKnight = new RedKnight(1,2)
        redKnight.moveUL()
        assert.deepEqual(redKnight.getPosition(), [0,0] )
    });

    it('should return final position', function () {
        const redKnight = new RedKnight(1,2)
        redKnight.moveUR()
        assert.deepEqual(redKnight.getPosition(), [2,0] )
    });

    it('should return final position', function () {
        const redKnight = new RedKnight(1,2)
        redKnight.moveR()
        assert.deepEqual(redKnight.getPosition(), [2,2] )
    });
});
