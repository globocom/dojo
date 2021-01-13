

function getContainersLength(listaOfContainers) {

	let listSorted = sortList(listaOfContainers)

	let resp = 1
	let limit = listSorted[0] + 4 
	for (let i =1; i< listSorted.length; i++){
		if(limit < listSorted[i])
		{
			resp++
			limit = 4 + listSorted[i]
		}
	}	
	return resp
}

function sortList(list){
	let listSorted = list
	for(let i = 0; i < listSorted.length; i++)
	{
		for(let j = i +1; j < listSorted.length; j++)
		{
			if(listSorted[j] < listSorted[i])
			{
				let aux = listSorted[i]
				listSorted[i] = listSorted[j]
				listSorted[j] = aux
			}
		}
	}
	return listSorted
}

module.exports = { getContainersLength, sortList };


// Lara -> Allan -> Juan

//[1,2,3]
// 10

// 16 18 17 17 19 2 0 9 10 13
// 0 2 9 10 13 16 17 17 18
// cont 
// [2,0]
// [9,10,13]
// [16,17,18,19]


// - ordenar
// - preencher os menores do que topo+4 em uma lista
// - retornar quantas listas