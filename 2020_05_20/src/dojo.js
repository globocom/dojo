function convertLetter(letter) {
  const numbers = {
    A: "2",
    B: "22",
    C: "222",
    D: "3",
    E: "33",
    F: "333",
    G: "4",
    H: "44",
    I: "444",
    J: "5",
    K: "55",
    L: "555",
    M: "6",
    N: "66",
    O: "666",
    P: "7",
    Q: "77",
    R: "777",
    S: "7777",
    T: "8",
    U: "88",
    V: "888",
    W: "9",
    X: "99",
    Y: "999",
    Z: "9999",
    " ": "0",
  };

  return numbers[letter];
}

function main(text) {
	let TextArr = text.split("_")
	
	/*
	for (i=0; text.length; i++){
		if text[i] text[i + 1]
	}
	
	s 7777
	e 33
	m 6
	p 
	r
	e

	// if (text === "oi mundo")
	// 	return '6664440688663666'
	// else if (text === 'oi')
	// 	return "666444"
	// else if (text === "sempre")
	// 	return "77773367_77733"
	*/
}
module.exports = { convertLetter, main };

