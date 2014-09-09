var ocupado = true;
var vazio = false;

var proximoMictorio = function(mictorios) {
  var intervalos = [],
      inicioIntervalo = null;

  for (var i = 0; i < mictorios.length; ++i) {
    if (mictorios[i] == vazio) {
      if (inicioIntervalo === null) {
        inicioIntervalo = i;
      }
    }
    else {
      if (inicioIntervalo !== null) {
        intervalos.push([inicioIntervalo, i - inicioIntervalo]);
        inicioIntervalo = null;
      }
    }
  }

  var inicioETamanho = _.max(intervalos, function(a){ return a[1] });

  return inicioETamanho[0];
  // return mictorios.indexOf(vazio);
};
