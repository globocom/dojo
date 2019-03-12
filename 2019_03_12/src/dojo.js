
function calcInnerSpaces(line) {
	if (line == 1) {
		return 0
	}
	var innerLines = 1
	for (var i = 2; i < line; i++) {
		innerLines += 2
	}
	return innerLines
}

function calcOuterSpace(line, totalLetters) {
	return totalLetters - line
}

function matrix(letter) {
	let result = []
	for (let i = 1; i <= letter.length; i++) {
		const outerSpace = calcOuterSpace(i, letter.length)
		const innerSpace = calcInnerSpaces(i)

		let resultLine = Array(outerSpace).fill(" ")
			.concat(letter[i - 1])
			.concat(Array(innerSpace).fill(" "))

		if (i > 1) {
			resultLine.push(letter[i - 1])
		}

		result.push(resultLine.concat(Array(outerSpace).fill(" ")))
	}
	return result
}

module.exports = {
	matrix,
	calcInnerSpaces,
	calcOuterSpace
};
