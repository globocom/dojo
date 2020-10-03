
function previousNumbersAreSmaller(visitorsPerDay, index) {
	return visitorsPerDay.filter((visitor,visitorIndex) => (visitor >= visitorsPerDay[index]) && (visitorIndex < index)).length === 0
}

function isLastDay(visitorsPerDay, index){
	return visitorsPerDay.length === index + 1
}

function isLargerThanFollowing(visitorsPerDay, index){
	if ((index + 1) !== visitorsPerDay.length)
		return visitorsPerDay[index] > visitorsPerDay[index + 1]
	return false
}

function main(visitorsPerDay){
	return visitorsPerDay.reduce((acc,visitors,index) => {
		if(previousNumbersAreSmaller(visitorsPerDay,index) &&
		(isLastDay(visitorsPerDay,index) ||
		isLargerThanFollowing(visitorsPerDay, index))){
			acc++
		}
		return acc
	}, 0)
}

module.exports = {previousNumbersAreSmaller, isLastDay, isLargerThanFollowing, main};
