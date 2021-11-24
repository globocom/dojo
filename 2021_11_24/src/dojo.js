
function createHashmap(array) {
	myHashMap = {}
	for (let i = 0; i<array.length ; i++){
		currentElement = array[i];

		if (currentElement in myHashMap){
			myHashMap[currentElement] += 1
		} else {
			myHashMap[currentElement] = 1
		}
	}
	return myHashMap
}

module.exports = createHashmap;