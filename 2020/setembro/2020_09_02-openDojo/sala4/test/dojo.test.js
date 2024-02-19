var assert = require('assert');
var {countdown}  = require('../src/dojo');

describe('Test True', function () {
    it('should return 1', function () {
        assert.strictEqual(countdown([9, 5, 6, 3, 2, 1], 3), 1);
    });

    it('should return 2', function () {
        assert.strictEqual(countdown([9, 5, 3, 2, 1, 6, 3, 2, 1], 2), 2);
    });

    it('should return 0', function () {
        assert.strictEqual(countdown([9, 5, 3], 2), 0);
    });
});

// Nathaly - Pedro - Rafaella - Matheus
// 3
// 1 - 2 - 3 - 2 - 1
// 1
// Exemplo: [1,2,3,4,5]



// A lista tem que ter tamanho igual ou maior ao tamanho do countdown
// Percorrer a lista verificando se o elemento sucessor é menor que o elemento corrente em 1 unidade.

// var list = 1 - 2 - 3 - 2 - 1;
