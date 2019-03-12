
function calcInnerSpaces(line) {
	if (line == 1) {
		return 0
	} 
	var innerLines = 1
	for(var i=2; i < line; i++) {
		innerLines += 2
	}
	return innerLines
}

function calcOuterSpace(line, totalLetters) {
	return totalLetters - line
}

function matrix(letter) {
	/** TODO */
	if (letter.length > 1) {
		return [
			["A"]
	   ["B", " ", "B"]
		]
	}
	return [[letter]]
}

module.exports = {
	matrix,
	calcInnerSpaces,
	calcOuterSpace
};
