
var input_final = `  785  516  744
272  511  358
801  791  693
572  150   74`

function main(x) {
	return true

}

function readLines(input) {
	count = 0
	let array_triangle = input.split('\n').map((linha) => linha.trim().split('  '))
	array_triangle.forEach((triangle) => {
		if (validate_sides(triangle[0], triangle[1], triangle[2]))
			count += 1
	})

	return count
}

function readColumn(input) {
	count = 0
	let array_triangle = input.split('\n').map((linha) => linha.trim().split('  '))

	for (i = 0; i < array_triangle.length; i += 3) {
		column1 = [array_triangle[i][0], array_triangle[i + 1][0], array_triangle[i + 2][0]]
		column2 = [array_triangle[i][1], array_triangle[i + 1][1], array_triangle[i + 2][1]]
		column3 = [array_triangle[i][2], array_triangle[i + 1][2], array_triangle[i + 2][2]]

		if (validate_sides(column1[0], column1[1], column1[2]))
			count += 1

		if (validate_sides(column2[0], column2[1], column2[2]))
			count += 1

		if (validate_sides(column3[0], column3[1], column3[2]))
			count += 1
	}

	return count
}

function validate_sides(var1, var2, var3) {
	if (parseInt(var1) + parseInt(var2) > parseInt(var3) &&
		parseInt(var2) + parseInt(var3) > parseInt(var1) &&
		parseInt(var3) + parseInt(var1) > parseInt(var2)) {
		return true
	} else {
		return false
	}

	// if(var1 == "25" && var2 == "10" && var3 == "25"){
	// 	return true
	// }else if(var1 == "2" && var2 == "10" && var3 == "25"){
	// 	return false
	// }
	// return false
}

module.exports = { main, validate_sides, readLines, readColumn };


/**
Raphel Rossi
Pedro Grosso
Christian
Bruna Costa
Pedro pereira
Fernando Guisso
 */

/**
 * 1 - Quebrar a linha em 3 valores
 * 2 - Fazer a soma do lado A com lado B
 * 2.1 - Verificar se é maior do que o lado C
 * 3 - Fazer a soma do lado B com lado C
 * 3.1 - Verificar se é maior do que o lado A
 * 4 - Fazer a soma do lado C com lado A
 * 4.1 - Verificar se é maior do que o lado B
 * 5 - Somar a quantidade de triangulos validos
 */