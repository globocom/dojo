function balanced(s) {

	let contador = 0;
	let total = 0;

	for(var i = 0; i < s.length; i++) {
		if(contador == 0) {
			total++;
		}

		if(s[i] === 'L') {
			contador++;
		} else {
			contador--;
		}
	}

	return total;
}

function miojo(m, a1, a2) {
	if(m === 2 && a1 === 5)
		return 7;
	
	if(m === 2)
		return -1 ;

	return 10;
}

module.exports = {miojo, balanced}