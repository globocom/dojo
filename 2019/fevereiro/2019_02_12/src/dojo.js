function main(expression) {
  let result = 0
  for (let i = 0; i < expression.length; i++) {
    result += getScore(expression[i])
    if (result < 0) {
      return false
    }
  }
  return result === 0
}

function getScore(char) {
  if (["(", ")"].includes(char)) {
    return char == ")" ? -1 : 1
  }
  return 0
}

module.exports = { main, getScore }
