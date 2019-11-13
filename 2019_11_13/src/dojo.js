
class RedKnight {
	constructor(x, y){
		this.positionX = x || 0
		this.positionY = y || 0
	}

	getPosition(){
		return [this.positionX, this.positionY]
	}

	moveLR(){
		this.positionX += 1
		this.positionY += 2
	}

	moveLL(){
		this.positionX -= 1
		this.positionY += 2
	}

	moveL(){
		this.positionX -= 2
	}

	moveUL(){
		this.positionX -= 1
		this.positionY -= 2
	}

	moveUR(){
		this.positionX += 1
		this.positionY -= 2
	}

	moveR(){
		this.positionX += 1
	}

}



module.exports = RedKnight;
