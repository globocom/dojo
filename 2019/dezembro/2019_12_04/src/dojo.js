function getLetter(number) {
	return String.fromCharCode(64+number)
}

function getCombinations(input) {
	let combinations = []
	for (let i = 0 ; i < input.lenght ; i++) {
		combinations.push(input[i])
	}
	// if (input === "25")
	// 	return [[2,5],[25]]
	// if (input === "13")
	// 	return [[1,3],[13]]
	// return [[1,2],[12]]
}

module.exports = {
	getLetter,
	getCombinations
};
