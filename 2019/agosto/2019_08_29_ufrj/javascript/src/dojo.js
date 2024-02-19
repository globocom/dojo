
function getUrlProtocol(url) {
	let url_split = url.split('://');
	let protocolo = url_split[0];
	return protocolo;
}

function getUrlDomain(url){
// 	if(url ==="ftp://facebook.com"){
// 		return "facebook.com";
// 	}
// 	if(url === "https://google.com"){
// 		return "google.com";
// 	}
// 	return "globo.com";
	let url_split = url.split('.');
	let url_split2 = url.split('://');

	let index = url_split.length;
	if( index === 3)
	{
		let protocolo = `${url_split[1]}.${url_split[2]}`;
		return protocolo;	
	}
	else
	{
		let protocolo = url_split2[1];
		return protocolo;
	}
	
}

module.exports = {getUrlProtocol, getUrlDomain};
