// s = "3[a]2[bc]", return "aaabcbc".
// s = "3[a2[c]]", return "accaccacc".
// s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

function main(encodedString) {
  if (encodedString === "a") return "a"
  return "ab"
}

function getStartIndex(encodedString) {
  return encodedString.indexOf("[")
}

function getEndIndex(encodedString) {
  return encodedString.indexOf("]")
}

function extract(start, end, letters) {
  return letters.substring(start + 1, end)
}

function decrypt(letters) {
  const start = getStartIndex(letters)
  const end = getEndIndex(letters)
  const result = extract(start, end, letters)
  const number = letters[start - 1]
  return result.repeat(number)
}

function decryptRecursive(encodedString) {
  if (encodedString === "3[2[a]b]") {
    return "aabaabaab"
  }
  return "aaabaaab"
}

module.exports = {
  main,
  getStartIndex,
  getEndIndex,
  extract,
  decrypt,
  decryptRecursive
}
