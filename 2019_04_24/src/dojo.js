
/**
 * Initialize your data structure here.
 */
var MyQueue = function() {
    this.values = []
};

/**
 * Push element x to the back of queue. 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
	// for(var i; i <= x; i++) {
	// 	if()
	// }
	// this.setValue(x)
	this.setValue([x,...this.values])
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
	return this.values.length === 0
};

MyQueue.prototype.getValue = function(){
	return this.values 
}

MyQueue.prototype.setValue = function(x){
	this.values = x
}

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

// function main() {
// 	return true
// }

module.exports = MyQueue;
