function interval() {
  let index = 0
  let array = [arguments[0]]
  const lastIndex = arguments.length - 1
  if (arguments.length > 1) {
    for (let i = 1; i < arguments.length; i++) {
      if (arguments[i] == arguments[i - 1] + 1) {
        array[1] = arguments[i]
      } else {
        array[1] = arguments[i - 1]
        return array
      }
    }
  }
  return [arguments[0], arguments[lastIndex]]
}

module.exports = interval
