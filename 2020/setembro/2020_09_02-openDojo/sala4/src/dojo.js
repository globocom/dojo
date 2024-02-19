
function countdown(lista, tamanhoDoCountDown) {
	var qtd = 0;
	var tamanho = 0;
	var anterior = lista[0];

	for (i = 1; i < lista.length; i++) {
		if(lista[i] === tamanhoDoCountDown) {
			for(j = i; j <= i + tamanhoDoCountDown - 1; j++){
			if(lista[i] === anterior - 1) {
				tamanho++;

				if (tamanho === tamanhoDoCountDown) {
					qtd++;
				}

			} else {
				tamanho = 0;
			}

		} else {
			tamanho = 0;
		}
	}

		anterior = lista[i];
	}

	return qtd;

/* 	if(lista.length == 3) {
		return 0;
	}

	if(tamanhoDoCountDown === 3) {
		return 1;
	}
		
	return 2; */
}

module.exports = {countdown};
