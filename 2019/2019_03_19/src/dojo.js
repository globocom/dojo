


function main(candidates, target) {
	const result = []
	if (candidates.includes(1))
		result.push(Array(target).fill(1))
	if (candidates.includes(target) && target != 1) {
		result.push([target])
	}

	const intermediateArray = intermediate(candidates, target)
	if (intermediateArray.length > 0) {
		// result.remove(intermediateArray)
		result.push(intermediateArray)
	}
	return result
}

function intermediate(candidates, target) {
	let sum = 0
	for (let i = 0; i < candidates.length; i++) {
		sum += candidates[i]
		if (sum == target) {
			return candidates.slice(0, i + 1)
		}
	}
	return []
}
module.exports = { main, intermediate };
