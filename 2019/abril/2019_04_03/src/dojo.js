function merge(l1, l2) {
  let expected = {
    val: l1.val,
    next: l2,
  }
  return expected
}

function createNode(args){
  if (args.length === 0)
    return null
  return expected = {
    val: args.shift(),
    next: createNode(args)
  }
}

function createLinkedList() {
  let args = []
  for (let i = 0; i < arguments.length; i++)
    args.push(arguments[i])
  let expected = createNode(args)
  return expected
}

module.exports = { merge, createLinkedList, createNode }
