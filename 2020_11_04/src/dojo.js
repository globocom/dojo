function makeMatrix(height, width, num_cameras, cameras_config) {
	let matrix = []

	
	// cria
	for(let i=0; i < height; i++){
		matrix.push([])
		for(let j=0; j < width; j++) {
			matrix[i].push(0)
		}
	} 
	console.log(matrix)
	// direita
	for(let i = 0; i < num_cameras; i++)
	{
		// leste
		for(let j = cameras_config[i][1]; j < width && j < cameras_config[i][2]; j++)
		{
			matrix[cameras_config[i][0]][j] = 1;
		}
		// oeste
		let k = 0
		for(let j = cameras_config[i][1]; j >= 0 && k < cameras_config[i][2]; j--, k++)
		{
			matrix[cameras_config[i][0]][j] = 1;
		}
		// sul
		for(let j = cameras_config[i][0]; j < height && j < cameras_config[i][2]; j++)
		{
			matrix[cameras_config[i][0]][j] = 1;
		}
		// norte
		let k = 0
		for(let j = cameras_config[i][1]; j >= 0 && k < cameras_config[i][2]; j--, k++)
		{
			matrix[cameras_config[i][0]][j] = 1;
		}

	}
	// 3 4 3

	
	//matrix[i][j] = 0
	// if (height === 5){
	// 	return [
    //         [0,0,1,0,0],
    //         [0,0,1,0,0],
    //         [1,1,1,1,1],
    //         [0,0,1,0,0],
    //         [0,0,1,0,0],
	// 		]
	// }
	// if(width === 22){
	// 	return [
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    //         [0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    //         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    //         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    //         ]
	// }
	// return [
	// 	[0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0],
	// 	[0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0],
	// 	[0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0],
	// 	[0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1],
	// 	[0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0],
	// 	[0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
	// 	[0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0],
	// 	[0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0],
	// 	[0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0],
	// 	[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
	// ]
}

module.exports = makeMatrix;
