function dojo(input) {
	let results = []
	let lines = [['q','w','e','r','t','y','u','i','o','p'],
	['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
	['z', 'x', 'c', 'v', 'b', 'n', 'm']]

	for (let y = 0; y < lines.length; y++) {
		for (let i = 0; i < input.length; i++) {
			if(checkRow(input[i], lines[y]))
			 results.push(input[i])
		}
	}
	return results
}

function checkRow(input, row) {
	for (let i = 0; i < input.length; i++) {
		if (row.indexOf(input[i].toLowerCase()) === -1)
			return false;
	}
	return true;
}

module.exports = {
	dojo,
	checkRow
};
