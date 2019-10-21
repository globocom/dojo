const letters = {
	A: 1,
	D: 1,
	O: 1,
	P: 1,
	Q: 1,
	R: 1,
	B: 2,
}

function letterHole(text) {
	return letters[text] || 0
}

function sumLetterHole(word) {
	return word.split("").reduce((accumulator, value) => accumulator += letterHole(value), 0)
}

module.exports = {
	letterHole,
	sumLetterHole
};
