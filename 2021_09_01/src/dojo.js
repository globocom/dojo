
function main() {
    return true
}

class MyHashMap {
    constructor() {
        this.myArr = new Array(8);
        this._length = 0;
    }

    _hash(key) {
        return key % 8;
    }

    set(key, value) {
        const hashKey = this._hash(key)
        if (this.myArr[hashKey] === undefined) {
            this.myArr[hashKey] = [];
        }
        // FIXME: verificar se já existe primeiro
        this.myArr[hashKey].push({ key: key, value: value });
        this._length++;
    }

    get(key) {
        if (this.myArr[this._hash(key)] === undefined) {
            return undefined
        }

        const myArr1 = this.myArr[this._hash(key)]

        for (var i = 0; i < myArr1.length; i++) {
            if (myArr1[i].key === key) {
                return myArr1[i].value
            }
        }
    }

    length() {
        return this._length;
    }
}

console.log(main())

myMap = new MyHashMap()
console.log(myMap._hash(3))
console.log(myMap._hash(11))
console.log(myMap._hash(1))
console.log(myMap.set(3, 89))
console.log(myMap.set(11, 20))
console.log(myMap.get(3))
console.log(myMap.get(11))
console.log(myMap.get(13))
console.log(myMap.length())

// myArr =
// [
//     undefined,
//     undefined,
//     undefined,
//     [
//         {key: 3,  value: 89},
//         {key: 11, value: 20},
//     ],
//     undefined,
//     undefined,
//     undefined,
//     undefined,
// ]



// Nicolas
// TCarreira
// Luciana
// Ingrid
// Christian
// Leonardo

///////////////////////////////
// MyHashMap
// MyHashMap.set(obj)
// MyHashMap.get(KEY)
// MyHashMap.length()
// MyHashMap.del(KEY)


// _array[8]
// MyHashMap._hash()

// resolver colisões?

// obj: {key: KEY, value: OBJ}\
// KEY: int()
// OBJ: anything
