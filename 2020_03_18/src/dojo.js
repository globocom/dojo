
function arraySort(array) {

	let auxiliar = 0
	let sorteArray = []

	if (array.length === 1){
		return array
	}
	else{
		for (let i = 0; i<array.length; i++){
			// for (let j = 1; j < array.length; j++){
			// 	if (array[i] > array[j]){
			// 		auxiliar = array[i]
			// 		array[i] = array[j]
			// 		array[j] = auxiliar
			// 	}
			// }
			if (sorteArray.length === 0){
				sorteArray.push(array[i])
			}
			else{
				if(array[i]>array[j]){
					sorteArray[i+1] = sortArray[i]
					sortArray[i] = sortArray[j]
				}
				
			}
		}
		return array
	}
}

module.exports = arraySort;