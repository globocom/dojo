var assert = require('assert');
var move = require('../src/dojo');


describe('Test True', function () {
    it ('should return the correct position 1', function(){
        let position = [0,0], direction= 'right'
        assert.deepEqual(move(position,direction),[0,1])
    })

    it ('should return the correct position 2', function(){
        let position = [0,0], direction= 'down'
        assert.deepEqual(move(position,direction),[1,0])
    })

    it ('should return the correct position 3', function(){
        let position = [1,2], direction= 'right'
        assert.deepEqual(move(position,direction),[1,3])
    })
    
    it ('should return next step', function(){
        let values = [1,2]
        assert.equal(nextStep(values[0], "right"), values[1])
    })
    // it('should return true', function () {
    //     let valuesMatrix=[[1,2],[2,3]]
    //     assert.deepEqual(getPath(valuesMatrix), [[1,2,3],[1,2,3]]);
    // });
    // it('should return true', function () {
    //     let valuesMatrix=[[1,5],[2,3]]
    //     assert.deepEqual(getPath(valuesMatrix), [[1,2,3],[1,2,3]]);
    // });
});

// [1,2]
// [2,3]