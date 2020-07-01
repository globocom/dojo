
function main(paths) {

	const dict = getCity(paths)
	let final_result = ""

	Object.keys(dict).map((key) => {
		if (dict[key])
			final_result = key
	})

	return final_result
}

function getCity(paths) {
	ans = {};

	for (let i=0; i<paths.length; i++) {
		let in_city = paths[i][0];
		let out_city = paths[i][1];

		ans[in_city] = false;

		if (ans[out_city] && ans[out_city]  === true){
			ans[out_city] = false;
		}
		else if (ans[out_city] === undefined){
			ans[out_city] = true
		}
	}

	return ans;
}

module.exports = {main, getCity};
