
// function getPath(matrix) {
// 	return [[1,2,3],[1,2,3]]
// }

function move(position,direction) {	
	return direction === "right" ? [position[0], position[1] + 1] : [position[0] + 1, position[1]]
}

module.exports = move;
