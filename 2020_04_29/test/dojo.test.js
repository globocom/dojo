// Ildefonso
// Ismael
// Pedro
// Elen
// Allan
// Juan
// Sami
// Bruna


var assert = require('assert');
var {calculateDistance, getCloseFriends} = require('../src/dojo');

describe('Test True', function () {
    let pessoa1 = {
        name: 'Pedrito',
        x: 0,
        y: 0
    }
    let pessoa2 = {
        name: 'Gabriela',
        x: 10,
        y: 0
    }
    let pessoa3 = {
        name: 'Sami',
        x: 0,
        y: 9
    }
    let pessoa4 = {
        name: 'Mateus',
        x: 0,
        y: 1
    }

    it('should return true', function () {
        assert.equal(calculateDistance(pessoa1, pessoa2), 10);
    });

    it('should return true', function () {
        pessoa1.x = 1
        assert.equal(calculateDistance(pessoa1, pessoa2), 9);
    });

    it('should return true', function () {
        pessoa1.x = 2
        assert.equal(calculateDistance(pessoa1, pessoa2), 8);
    });

    it('should return true', function () {
        pessoa1.x = 0
        assert.deepEqual(getCloseFriends(pessoa1,[pessoa2, pessoa3, pessoa4] ), ['Mateus', 'Sami']);
    });
});


////raiz ( (a.x - b.x)^2 + (a.y - b.y)^2 )

// 5         B
// 4       .
// 3      .   
// 2     .
// 1   A      
//   1 2 3 4 5  

//Arrasou Juan <3 