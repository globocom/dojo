function replaceMatrix(matrix) {
	matrix.map((line) => {
		for (let i = 0; i < line.length; i++){
			const value = line[i] === 'G' ? 1 : 0
			line.splice(i, 1, value)
		}
		return line
	})
	return matrix
	
}

function validadeMatrix(matrix) {
	return [
		[1,1,1,1,1,1],
		[1,0,0,0,1,0],
		[1,1,1,1,5,1],
		[1,1,0,0,1,0],
		[1,1,1,1,1,1]
	]
}


/* 
	[m,l],[m+1,l],[m+2,l]
	[m,l+1],[m+1,l+1],[m+1,l+1]
	[m,l+2],[m+1,l+2],[m+1,l+2]
*/


module.exports = {replaceMatrix, validadeMatrix};
