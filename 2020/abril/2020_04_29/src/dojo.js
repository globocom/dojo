
function calculateDistance(a, b) {
	var lat = (a.x - b.x)**2;
	var lon = (a.y - b.y)**2;

	var distance = Math.sqrt(lat+lon);

	return distance;
}

function getCloseFriends(pessoa1, amigos){
	amigos.sort(function(amigoA, amigoB){
		let distA = calculateDistance(pessoa1, amigoA) 
		let distB = calculateDistance(pessoa1, amigoB)
		if (distA > distB) {
			return 1 
		}
		if (distA < distB) {
			return -1 
		}

		return 0
	})

	let amigosFiltered = amigos.slice(0,2)

	return amigosFiltered.map(amigo => amigo.name)
}

module.exports = {
	calculateDistance,
	getCloseFriends
};

// arr.sort(function(a,b){
// 	if (a < b)
// 		return -1
// 	if (a > b)
// 		return 1
	
// 	return 0
// });

//O método slice() retorna uma cópia de parte de um array a partir de um subarray criado entre as posições início(begin) e fim(end)(fim não é necessário) de um array original. O Array original não é modificado.