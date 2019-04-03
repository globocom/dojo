function merge(l1, l2) {
  let expected = {
    val: l1.val,
    next: l2,
  }
  return expected
}

function createLinkedList(value, value2, value3) {
  let expected = {
    val: value,
    next: null,
  }

  if (value2) {
    expected.next = {
      val: value2,
      next: null,
    }
  }

  if (value3) {
    expected.next.next = {
      val: value3,
      next: null,
    }
  }

  return expected
}

module.exports = { merge, createLinkedList }
