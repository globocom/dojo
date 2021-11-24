
// Count elements
let myHashMap = {} 
for (let i = 0 ; i < nums.length ; i++){
    currentElement = nums[i];

    if (currentElement in myHashMap){
        myHashMap[currentElement] += 1
    } else {
        myHashMap[currentElement] = 1
    }
}

// Object to array, then sort the array
var sortable = [];
for (element in myHashMap) {
    sortable.push([element, myHashMap[element]]);
}
sortable.sort(function(a, b) {
    return b[1] - a[1];
});

// get top K
result = []
for (let i=0 ; i < k ; i++){
    result.push(parseInt(sortable[i][0]));
}


return result