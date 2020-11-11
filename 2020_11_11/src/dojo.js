function toDecimal(hexadecimal) {
  const dic = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    A: 10,
    B: 11,
    C: 12,
    D: 13,
    E: 14,
    F: 15,
  };

  let hexsplitted = hexadecimal.split("");
  hexsplitted = hexsplitted.reverse();

  return hexsplitted.reduce((acc, value, index, arr) => {
    const hexValue = dic[value];
    acc += hexValue * Math.pow(16, index);
    return acc;
  }, 0);
}

function palindromo(capicua) {
  const palin = capicua.toString();
  let tam = palin.length - 1;
  for (let i = 0; i < tam; i++, tam--) {
    if (palin[i] != palin[tam]) return false;
  }
  return true;
}

module.exports = {
  toDecimal,
  palindromo,
};
