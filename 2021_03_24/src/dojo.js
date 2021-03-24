

function main(arr, K) {
	let countdown = 0;
	let previous = 0;
	for (let i=arr.length -1; i>=0 ; i-- ) {		
		if ( arr[i] === previous + 1){
			previous++;
			console.log(i, previous)
			if (previous === K){
				countdown++;
				previous = 0;
			}
		}
		else
		{
			if(arr[i] == 1) {
				previous = arr[i];
			} else {
				previous = 0;2
			}
		}
	}

	return countdown;
}

module.exports = main;


/*
[3,2,1,2,1]
Steps:[3,2,2,1,1]
- (arr, k) = [5,7,6,3,2,1,3,2], 3
    return -> 1
	[3,2,2,1,1]
- (arr, k) = [5,6,7,3,2,1,3,2], 3
	return -> 1
- (arr, k) = [7,3,2,1,3,2,1], 3
	return -> 2

Tiago - Juan - Lara - Sami
*/