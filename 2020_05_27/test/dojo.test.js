var assert = require("assert");
var {replaceMatrix, validadeMatrix} = require("../src/dojo");

describe("Test True", function () {
    it("should return true", function () {
        let matrix = [
            ['B', 'G', 'B'],
            ['G', 'G', 'G'],
            ['B', 'G', 'B']
        ]

        assert.deepEqual(replaceMatrix(matrix),[[0,1,0],[1,1,1],[0,1,0]]);
    });

    it("should return true 2", function () {
        let matrix = [
            ['G','G','G','G','G','G'],
            ['G','B','B','B','G','B'],
            ['G','G','G','G','G','G'],
            ['G','G','B','B','G','B'],
            ['G','G','G','G','G','G'],
        ]
    
        assert.deepEqual(replaceMatrix(matrix),[
            [1,1,1,1,1,1],
            [1,0,0,0,1,0],
            [1,1,1,1,1,1],
            [1,1,0,0,1,0],
            [1,1,1,1,1,1]
        ]);
    });

    it("should return true 3", function () {
        let matrix = [['B']]
    
        assert.deepEqual(replaceMatrix(matrix),[[0]]);
    });

    it("should return true 4", function () {
        let matrix = [
            [1,1,1,1,1,1],
            [1,0,0,0,1,0],
            [1,1,1,1,1,1],
            [1,1,0,0,1,0],
            [1,1,1,1,1,1]
        ]
    
        assert.deepEqual(validadeMatrix(matrix),[
            [1,1,1,1,1,1],
            [1,0,0,0,1,0],
            [1,1,1,1,5,1],
            [1,1,0,0,1,0],
            [1,1,1,1,1,1]
        ]);
    });
});

/*
G G G G G G | G G G G G G |  
G B B B G B | G B B B | B |
G G G G G G | G G G - + - | 
G G B B G B | G G B B | B |
G G G G G G | G G G G G G |
*/

// let bla = [
    // [G','G','G','G','G','G'],
    // ['G','B','B','B','G','B'],
    // ['G','G','G','G','G','G'],
    // ['G','G','B','B','G','B'],
    // ['G','G','G' ,'G','G','G'],
// ]
// let bla = [
    // ['1','1','1','1','1','1'],
    // ['1','0','0','0','1','0'],
    // ['1','1','1','1','1','1'],
    // ['1','1','0','0','1','0'],
    // ['1','1','1','1','1','1'],
// ]

// let bla2 = [
//     ['G']
// ]

// let bla3 = [
//     ['B', 'G', 'B'],
//     ['G', 'G', 'G'],
//     ['B', 'G', 'B']
// ]


// Juan Matheus Ingrid Sami Icaro Elen