function stepLog(num) {
  return Math.ceil(Math.log2(num) + 1);
}

function stepToReduce(num) {
  //   return Math.ceil(Math.log2(num)) +1;
  let count = 0;
  let temp = num;
  while (temp > 0) {
    temp = calcNumber(temp);
    count++;
  }
  return count;
  //   if (num == 2) {
  //     return 2;
  //   } else if (num == 4) {
  //     return 3;
  //   }
  //   return 4;
}

function isOddNumber(num) {
  return num % 2 != 0;
}

function calcNumber(num) {
  if (isOddNumber(num)) {
    return num - 1;
  }
  return num / 2;
}

module.exports = { stepToReduce, isOddNumber, calcNumber };
