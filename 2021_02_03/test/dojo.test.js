var assert = require('assert');
var {som, main, winningNumber, ordering} = require('../src/dojo');


describe('Test True', function () {
    
    it('som test 1', function () {
        assert.equal(som("A"),2);
    });

    it('som test 2', function () {
        assert.equal(som("Ab"), 5);
    });

    it('som test 3', function () {
        assert.equal(som("PauL"), 54);
    });
    
    it('winningNumber test 1', function () {
        assert.equal(winningNumber(10,1), 10);
    });

    it('winningNumber test 2', function () {
        assert.equal(winningNumber(5,3), 15);
    });

    it('winningNumber test 2', function () {
        assert.equal(winningNumber(1,3), 3);
    });

    it('ordering test 1', function () {
        assert.deepEqual(ordering({'a': 2, 'ba': 50, 'c': 15}), ['ba','c','a']);
    });

    it('ordering test 2', function () {
        assert.deepEqual(ordering({'a': 2, 'ba': 2, 'c': 15}), ['c','a', 'ba']);
    });

    it('ordering test 3', function () {
        assert.deepEqual(ordering({'a': 60, 'ba': 2, 'c': 15}), ['a','c', 'ba']);
    });
    it('main 1', function () {
        assert.equal(main(["COLIN","AMANDBA","AMANDAB","CAROL","PauL","JOSEPH"], [1, 4, 4, 5, 2, 1], 4), "PauL");
    });
});

//names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
//weights: [1, 4, 4, 5, 2, 1]

// Tiago - Elen - Pedro - Juan - Marina - Ingrid - Sami

// pseudo-algoritmo:

// som = len(name) + sum( ord(letter), ...   )
//                    sum()
//                          ord()
// winning_number = som * weight
// order by winning_number desc, name asc
// return name at N (starting at 1)