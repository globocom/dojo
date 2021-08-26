var assert = require('assert');
var { main, checkAndSwap, insideBubble, bubbleSort } = require('../src/dojo');

const myArr = [5, 6, 3, 1, 8, 7, 2, 4];

describe('Test True', function () {
    it('should return true', function () {
        assert.equal(main(), true);
    });

    it('should NOT swap element 0-1', function () {
        assert.deepEqual(
            checkAndSwap(myArr, 0),
            [5, 6, 3, 1, 8, 7, 2, 4],
        );
    });
    it('should swap element 1-2', function () {
        assert.deepEqual(
            checkAndSwap(myArr, 1),
            [5, 3, 6, 1, 8, 7, 2, 4],
        );
    });
    it('should not swap element 6-7', function () {
        assert.deepEqual(
            checkAndSwap(myArr, 6),
            [5, 6, 3, 1, 8, 7, 2, 4],
        );
    });

    it('bubble first iter until 3', function () {
        assert.deepEqual(
            insideBubble(myArr, 3),
            [5, 3, 1, 6, 8, 7, 2, 4],
        );
    });
    it('bubble first iter until 5', function () {
        assert.deepEqual(
            insideBubble(myArr, 5),
            [5, 3, 1, 6, 7, 8, 2, 4],
        );
    });
    it('bubble first iter complete', function () {
        assert.deepEqual(
            insideBubble(myArr, 7),
            [5, 3, 1, 6, 7, 2, 4, 8],
        );
    });


    it('bubble sort mtf', function () {
        assert.deepEqual(
            bubbleSort(myArr),
            [1, 2, 3, 4, 5, 6, 7, 8],
        );
    });


});


// i:   0  1  2  3  4  5  6  7
// arr:  [5, 6, 3, 1, 8, 7, 2, 4]
// until: arr.length`

// - iterar until entre arr.length até 1:
//     - iterar arr ( 0 <= i < until ), e para cada elemento arr[i]:
//         - comparar 2 elementos (i, i+1)
//             - se o primeiro elemento for maior, troca

