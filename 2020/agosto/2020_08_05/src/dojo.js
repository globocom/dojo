	
function countBreaks(pitch, allienPitch) {
	let notes = ['A', 'B', 'C', 'D']
	let current = notes.indexOf(allienPitch);
	// fazer um for no pitch
	// se o num for maior que o anterior e a nota é a última de notes, quebra
	// se não, note vai ser a próxima nota
	// se o num for menor que o anterior e a nota é a primeira de notes, quebra
	// se não, note vai ser a nota anterior
	return pitch.reduce(function(acumulador, valorAtual, index, pitch) {
		if(index !== 0) {
			if(pitch[index-1] < valorAtual) {
				if (current === notes.length-1){
					acumulador++;
					current = 0;
				} else {
					current++;
				}	
			} 
			if(pitch[index-1] > valorAtual) {
				if (current === 0){
					acumulador++;
					current = notes.length-1;
				} else {
					current--;
				}	
			}
		}
		return acumulador;
	}, 0)
}

module.exports = countBreaks;

//[4, 6, 8, 12].indexOf(valor)

// [0, 1, 2, 3, 4].reduce(function(acumulador, valorAtual, index, array) {
//   return acumulador + valorAtual;
// });
// 10