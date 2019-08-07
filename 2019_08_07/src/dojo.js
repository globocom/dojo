function main(quantity, symbols) {
	const array = []
	for (let i = 0; i < quantity; i++) {
		if (i < quantity - symbols) {
			array.push(" ")
			continue
		}
		array.push("*")
	}
	return array
}

module.exports = main;
