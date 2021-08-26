
function main() {
	return true
}

function checkAndSwap(arr, i) {
	var arrAux = [...arr];

	if (arrAux[i] > arrAux[i + 1]) {
		const tmp = arrAux[i];
		arrAux[i] = arrAux[i + 1];
		arrAux[i + 1] = tmp;
		return arrAux;
	}
	return arr;
}

function insideBubble(arr, until) {
	var arrAux = [...arr];

	for (var i = 0; i < until; i++) {
		arrAux = checkAndSwap(arrAux, i);
	}

	return arrAux;
}

function bubbleSort(arr) {
	var myArr = [...arr];
	for (var i = myArr.length; i > 0; i--) {
		myArr = insideBubble(myArr, i);
	}
	return myArr;
}

module.exports = { main, checkAndSwap, insideBubble, bubbleSort };
