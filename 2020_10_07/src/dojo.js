
function transformWord(word) {

	let usedLetters = {}
	let newWord = []
	let count = 0
	let wordList = [...word]

	wordList.forEach(letter => {

		if (!usedLetters[letter]) {
			count += 1
			usedLetters[letter] = count
		}

		newWord.push(usedLetters[letter])
	})
	return newWord.join('|')
}

function main(pattern, wordList) {

	const transformPattern = transformWord(pattern)

	return wordList.reduce((acc, currentValue) => {
		if (transformWord(currentValue) === transformPattern)
			acc.push(currentValue)
		return acc
	}, [])
	
}

module.exports = { transformWord, main };