function dojo(frase) {
	var fraseArray = "";
	for (var i = 0; i < frase.length; i++) {
	  var c = frase[i].charCodeAt(0);
  
	  if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122)) {
		c += 3;
	  }
	  fraseArray += String.fromCharCode(c);
	}
	return fraseArray;
  }
  function inverte(frase) {
	var novaFrase = "";
	for (var i = frase.length - 1; i >= 0; i--) {
	  novaFrase += frase[i];
	}
	return novaFrase;
  }
  
  function extra(frase) {
	var fraseArray = "";
	for (var i = 0; i < frase.length; i++) {
	  var c = frase[i].charCodeAt(0);
	  if (i >= Math.floor(frase.length / 2)) {
		c -= 1;
	  }
	  fraseArray += String.fromCharCode(c);
	}
	return fraseArray;
  }
  
  function main(frase) {
	var novaFrase = dojo(frase);
	novaFrase = inverte(novaFrase);
	novaFrase = extra(novaFrase);
	return novaFrase;
  }
  
  module.exports = { dojo, inverte, extra, main };
  