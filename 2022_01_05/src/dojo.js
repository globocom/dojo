
function main() {
  return true
}

// const array1 = [1, 2, 3, 4];
// const reducer = (previousValue, currentValue) => previousValue + currentValue;

// // 1 + 2 + 3 + 4
// console.log(array1.reduce(reducer));
// // expected output: 10

// // 5 + 1 + 2 + 3 + 4
// console.log(array1.reduce(reducer, 5));
// // expected output: 15


function getFloor(s) {
//   sum = 0
//  for (i=0; i<s.length; i++) {
//   if (s[i] === "(") {
//     sum += 1
//   } else {
//     sum -= 1
//   }
//  }


  return s.split("").reduce((p, c) => p + (c === "(" ? 1:-1), 0)
}

function getBasement(s) {

  sum = 0
  for (i=0; i<s.length; i++) {
    if (s[i] === "(") {
      sum += 1
    } else {
      sum -= 1
    }
    if (sum < 0) return i+1
  }
  return sum

}

module.exports = {main, getFloor, getBasement};
