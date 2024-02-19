function main(text) {
	let hashedValue = getValueToHash(text);
	hashedValue = incAscValue(hashedValue);
	hashedValue = codeReverse(hashedValue);
	hashedValue = shiftFromMiddleToEnd(hashedValue);
  
	return convertAsciiToString(hashedValue);
  }
  
  function getValueToHash(valueToHash) {
	let values = [];
	for (let i = 0; i < valueToHash.length; i++) {
	  values.push(valueToHash.charCodeAt(i));
	}
	return values;
  }
  
  function isASCIILetter(value) {
	return (value >= 65 && value < 90) || (value >= 97 && value <= 122);
  }
  
  //First step
  function incAscValue(ascList) {
	let list = [];
	ascList.map(value => {
	  if (isASCIILetter(value)) {
		list.push(value + 3);
	  } else {
		list.push(value);
	  }
	  return list;
	});
	return list;
  }
  
  //Second step
  function codeReverse(codeNumbers) {
	let newString = [];
	for (let i = codeNumbers.length - 1; i >= 0; i--) {
	  newString.push(codeNumbers[i]);
	}
	return newString;
  }
  
  //Third step
  function shiftFromMiddleToEnd(codeNumbers) {
	let list = [];
	const halfIndex = Math.floor(codeNumbers.length / 2);
	for (let i = 0; i < codeNumbers.length; i++) {
	  if (i >= halfIndex) {
		list.push(codeNumbers[i] - 1);
	  } else {
		list.push(codeNumbers[i]);
	  }
	}
	return list;
  }
  
  // Last step
  function convertAsciiToString(codeNumbers) {
	return String.fromCharCode(...codeNumbers);
  }
  
  module.exports = {
	main,
	getValueToHash,
	incAscValue,
	codeReverse,
	shiftFromMiddleToEnd,
	convertAsciiToString,
	isASCIILetter
  };
  