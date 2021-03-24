var assert = require('assert');
var dojo = require('../src/dojo');


describe('Test 1', function () {
    it('should return 1', function () {
           assert.equal(dojo([5,7,6,3,2,1,3,2], 3), 1);
       });
   });
   
describe('Test 2', function () {
    it('should return 2', function () {
        assert.equal(dojo([7,3,2,1,3,2,1], 3), 2);
    });
    it('should return 3', function () {
        assert.equal(dojo([3,2,1,2,1], 3), 1);
    });
    it('should return 4', function () {
        assert.equal(dojo([3,2,2,1,1], 3), 0);
    });
});


