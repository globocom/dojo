
function verifySum(a, b, c) {
	return sum(a, b) === c
}

function sum(a, b) {
	return a + b
}

function main(arr, num) {

	for(let i = 0; i<arr.length;i++){
		for (let y = 0; y < arr.length; y++) {
			if(i !== y) {
				if (verifySum(arr[i], arr[y], num)){
					return [i, y]
				}
			}
			
			
		}
	}
	return []
}


module.exports = { sum, verifySum, main };
