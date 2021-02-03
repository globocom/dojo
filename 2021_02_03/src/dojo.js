
function main(names, weight, n) {
	draws = {}
	for (let i=0; i<names.length; i++) {
		draws[names[i]] = winningNumber(som(names[i]), weight[i])
	}
	orderedDraws = ordering(draws)
	return orderedDraws[n-1]
}

function som(name) {
	const tam = name.length
	let contName = 0;

	for (const letter of name) {
		contName += letter.toUpperCase().charCodeAt()-64
	}

	const res = tam + contName;

	return res;
}

function winningNumber(son, weight) {
	return son * weight
}

function ordering(list) {
	return Object.keys(list).sort(function(a,b){return list[b]-list[a]})
	
}

module.exports = {main, som,winningNumber, ordering};
