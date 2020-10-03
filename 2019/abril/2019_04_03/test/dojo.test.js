var assert = require("assert")
var dojo = require("../src/dojo")

describe("Test True", function() {
  it("should create a node", function() {
    let expected = {
      val: 1,
      next: null,
    }
    assert.deepEqual(dojo.createNode([1]), expected)
  })
  it("should create two nodes", function() {
    let expected = {
      val: 1,
      next: {
        val: 2,
        next: null,
      },
    }
    assert.deepEqual(dojo.createNode([1, 2]), expected)
  })
  it("should create three nodes", function() {
    let expected = {
      val: 1,
      next: {
        val: 2,
        next: {
          val: 3,
          next: null,
        },
      },
    }
    assert.deepEqual(dojo.createNode([1, 2, 3]), expected)
  })
  it("should create a linked list with one node", function() {
    let expected = {
      val: 1,
      next: null,
    }
    assert.deepEqual(dojo.createLinkedList(1), expected)
  })
  it("should create a linked list with two nodes", function() {
    let expected = {
      val: 1,
      next: {
        val: 2,
        next: null,
      },
    }
    assert.deepEqual(dojo.createLinkedList(1, 2), expected)
  })
  it("should create a linked link with three nodes", function() {
    let expected = {
      val: 1,
      next: {
        val: 2,
        next: {
          val: 3,
          next: null,
        },
      },
    }
    assert.deepEqual(dojo.createLinkedList(1, 2, 3), expected)
  })
  it("should merge two linked lists", function() {
    let list1 = {
      val: 1,
      next: null,
    }
    let list2 = {
      val: 2,
      next: null,
    }
    let expected = {
      val: list1.val,
      next: list2,
    }
    assert.deepEqual(dojo.merge(list1, list2), expected)
  })
})
