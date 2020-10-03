
function getLetters(letter) {
	const alphabet = ['A', 'B','C', 'D', 'E']
	const letterIndex = alphabet.indexOf(letter)
	return alphabet.slice(0, letterIndex+1)
}

function getMatrixSize(letter){
	return (2 * getLetters(letter).length) - 1
}

module.exports = {getLetters, getMatrixSize};
