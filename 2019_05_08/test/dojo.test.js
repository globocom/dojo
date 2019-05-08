var assert = require('assert');
var catDistance = require('../src/dojo').catDistance;
var calculateWinner = require('../src/dojo').calculateWinner;
var main = require('../src/dojo').main;


describe('Test True', function () {
    it('should return 2', function () {
        // let positions = [1,2,3] 
        assert.equal(catDistance(1,3), 2);
    });
    it('should return 1', function () {
        // let positions = [1,2,3] 
        assert.equal(catDistance(2,3), 1);
    });
    it('should return 2', function () {
        // let positions = [1,2,3] 
        assert.equal(catDistance(3,1), 2);
    });
    it('should return cat b', function () {
        let positions = [1,2,3] 
        assert.equal(calculateWinner(positions), "cat B");
    });
    it('should return cat a', function () {
        let positions = [2,1,3] 
        assert.equal(calculateWinner(positions), "cat A");
    });
    it('should return cat a', function () {
        let positions = [5,1,3] 
        assert.equal(calculateWinner(positions), "mouse C");
    });
    it('should return cat a', function () {
        let positions = [5,1,3]
        let positions2 = [6,2,3] 
        assert.deepEqual(main(positions, positions2), ["mouse C", "cat B"]);
    });
    it('should return cat a', function () {
        let positions = [5,1,3]
        let positions2 = [2,6,3] 
        assert.deepEqual(main(positions, positions2), ["mouse C", "cat A"]);
    });
    it('should return cat a', function () {
        let positions = [5,1,3]
        let positions2 = [2,6,3] 
        let positions3 = [1,2,3] 
        assert.deepEqual(main(positions, positions2, positions3), ["mouse C", "cat A", "cat B"]);
    });
});
