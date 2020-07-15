function main() {
	return true;
  }
  
  function getValueToHash(valueToHash) {
	let values = [];
	for (let i = 0; i < valueToHash.length; i++) {
	  values.push(valueToHash.charCodeAt(i));
	}
	return values;
  }
  
  function incAscValue(ascList) {
	let list = [];
	ascList.map(value => {
	  if ((value >= 65 && value < 90) || (value >= 97 && value <= 122)) {
		list.push(value + 3);
	  } else {
		list.push(value);
	  }
	  return list;
	});
	return list;
  }
  
  module.exports = {
	main,
	getValueToHash,
	incAscValue
  };
  