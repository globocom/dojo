function sortArray(array) {
  return array.sort();
}

function checkDifference(num1, num2) {
  if (Math.abs(num1 - num2) <= 1) {
    return true;
  } else {
    return false;
  }
}

function biggestArray(arrays) {
  return arrays.reduce((prev, current) => {
    if (current.length > prev) return current.length;
    return prev;
  }, 0);
}
module.exports = {
  sortArray,
  checkDifference,
  biggestArray
};
