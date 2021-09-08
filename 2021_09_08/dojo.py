def main():
    return True


class MyHashMap:
    def __init__(self):
        self._len = 0
        self.arr = [None] * 8

    def __len__(self):  # dunder
        return self._len

    @classmethod
    def _hash(klass, key):
        return key % 8

    def set(self, key, value):
        hashed_key = MyHashMap._hash(key)
        if self.arr[hashed_key] is None:
            self.arr[hashed_key] = []

        for element in self.arr[hashed_key]:
            if element["key"] == key:
                element["value"] = value
                return

        self.arr[hashed_key].append({"key": key, "value": value})
        self._len += 1

    def get(self, key):
        if self.arr[MyHashMap._hash(key)] is None:
            return None
        myArr = self.arr[MyHashMap._hash(key)]
        for element in myArr:
            if element["key"] == key:
                return element["value"]

    def delete(self, key):
        index = MyHashMap._hash(key)
        myArr = self.arr[MyHashMap._hash(key)]

        for index, element in enumerate(myArr):
            if element["key"] == key:
                self._len -= 1
                self.arr[MyHashMap._hash(key)] = [*myArr[:index], *myArr[index + 1 :]]


# MyHashMap
#  _hash()
#  set()
#  get()
#  len()
#  del()

############## ordem:
# tcarreira
# chris
# leo
# thiago
# luciana
