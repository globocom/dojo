
function parseInput(myInput){
	let myInputArray = myInput.split("\n");
	return myInputArray.map(e => {return parseInt(e)});
}

function countIncrements(arrayInput) {
	return arrayInput.reduce((acc, value, index, array) => {
		if (value > array[index - 1]) {
			acc +=1
		}
		return acc
	},0)
}

async function readFile(filename) {
	const fs = require('fs').promises;
	return await fs.readFile(filename);
}

function main(myinput) {
	const arr = parseInput(myinput);
	return countIncrements(arr);
}

module.exports = {parseInput, countIncrements, readFile, main};