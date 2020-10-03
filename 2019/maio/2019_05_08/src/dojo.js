
function catDistance(cat, mouse) {
	return Math.abs(mouse - cat)
}

function calculateWinner(arr) {
	let catA = catDistance(arr[0], arr[2])
	let catB = catDistance(arr[1], arr[2])
	if (catA > catB) {
		return "cat B"
	}
	if(catA < catB) {
		return "cat A"
	}
	return "mouse C"
}

function main() {
	return Array.prototype.map.call(arguments, (position) => {
		return calculateWinner(position)
	})
}


module.exports = {
	catDistance,
	calculateWinner,
	main
};
