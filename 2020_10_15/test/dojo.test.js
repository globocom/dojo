var assert = require('assert');
var {miojo, balanced} = require('../src/dojo');


describe('Test True', function () {

    //Sring Balanceada
    it('should return 4', function () {
        assert.equal(balanced('RLRRLLRLRL'), 4);
    });

    it('should return 2', function () {
        assert.equal(balanced('RLRL'), 2);

    });

    it('should return 6', function () {
        assert.equal(balanced('RLRLRLRLRLRL'), 6);
    });

    it('should return 3', function () {
        assert.equal(balanced('RLLLLRRRLR'), 3);
    });

    it('should return 1', function () {
        assert.equal(balanced('LLLLRRRR'), 1);
    });

    //Miojo
    it('should return 10', function () {
            assert.equal(miojo(3,5,7), 10);
        });
    it('should return -1', function () {
            assert.equal(miojo(2,6,9), -1);
        });
    it('should return 7', function () {
            assert.equal(miojo(2,5,7), 7);

        });
})

// Joaquim
// Matheus
// Diana
// kaline