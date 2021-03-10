package main

import (
	"fmt"
	"math"
	"regexp"
	"strings"
	"unicode/utf8"
)

func fFunction(arg1 int, arg2 bool, arg3 string) (string, bool, int) {
	return arg3, arg2, arg1
}
func fFunction2(arg int) (int, error) {
	return 0, fmt.Errorf("this is an error message")
	// return 42, nil
}

func main() {
	////////////////////////////////////////////////////////////////////////////
	// Language idiosyncratics
	////////////////////////////////////////////////////////////////////////////
	const idiosyncratics = `
	- strong typing - variables implicit type with ':=' 
	- you cannot redeclare variables (:= only the first time)
	- on variable declaration, Type comes after variableName
	- indentation should be tabs, not spaces, but no real requirements
	- all variables MUST be used. Does not compile with unused variables
	- camelCaseIsRecommended
`

	////////////////////////////////////////////////////////////////////////////
	// Types
	// declare var (explicit type):  var <varName> <type>
	//                               <varName> = <value>
	// declare var (explicit type):  var <varName> <type> = <value>
	// declare var (implicit type):  <varName> := <value> // type depends on <value>
	////////////////////////////////////////////////////////////////////////////
	tBool := true     // implicit type declaration with := for booleans
	tStr := "abc"     // implicit type declaration with := for strings
	tInt := 123       // implicit type declaration with := for integers
	tFloat := 1234.56 // or 1.23456e3  // implicit with := for floats
	type tStruct struct {
		name  string
		value int
	}
	structVar := tStruct{name: "My Name", value: 42} // access: structVar.name
	tPointer := &structVar                           // Pointers in Go
	var tNil *tStruct = nil                          // Null in Go is nil, for objects, maps...
	// Both tStruct and *tStruct typed variables are accessed with v.name

	tSlice := []int{1, 2, 3, 4} // Arrays and Slices are not the same. For dojo, use slices
	tMap := map[string]int{     // Maps tMap["key"] = value
		"hello": 1,
		"world": 10,
	} // implicit assignment

	////////////////////////////////////////////////////////////////////////////
	// Maths & Basics
	////////////////////////////////////////////////////////////////////////////
	tInt++                                   // increment by one
	powered := math.Pow(2, 8)                // 256
	modDivision := 13 % 5                    // 3
	floored := math.Floor(42.8)              // 2
	ceiled := math.Ceil(41.2)                // 2
	roundedStr := fmt.Sprintf("%.2f", 2.255) // 2.26 - go is dirty for decimal places -.-
	rounded := math.Round(2.255*100) / 100   // 2.26 - go is dirty for decimal places -.-

	////////////////////////////////////////////////////////////////////////////
	// Functions (declared outside main)
	////////////////////////////////////////////////////////////////////////////
	fFunction(2, true, "string")                 // all arguments are mandatory
	_, _, newInt := fFunction(2, true, "string") // ignore returned values with _

	// short syntax for error checking: if <call_funcion>; <if clause> { ... }
	if _, err := fFunction2(0); err != nil {
		fmt.Println("Handle errors like this:", err)
	}

	////////////////////////////////////////////////////////////////////////////
	// String manipulation
	////////////////////////////////////////////////////////////////////////////
	c := "concatenate" + " strings" // only strings
	formattedString := fmt.Sprintf("string: %s, int: %d, float: %.2f, anything?: %v, expanded: %+v, type: %T\n",
		"string", 42, 123.45, &tStruct{}, structVar, 42.5,
	)
	_ = strings.ToUpper("Everything to Uppercase")
	_ = strings.ToLower("Everything to Lowercase")
	_ = strings.TrimSpace("  no spaces before or after   \n")
	splitString := strings.Split("split, a, string", ", ")
	_ = strings.Join(splitString, ", ")
	stringLength := utf8.RuneCountInString("ç") // 1
	stringLengthBytes := len("ç")               // 2 !!! ok when dealing with ascii only
	_ = strings.ReplaceAll("abc", "bc", "eiou") // abc -> aeiou

	////////////////////////////////////////////////////////////////////////////
	// Conditionals
	////////////////////////////////////////////////////////////////////////////
	if true {
		fmt.Println("operators: ==, !=, >, >=, <, <=")
	} else if (tNil == nil || structVar == tStruct{name: "My Name", value: 42}) && "bool" == "only" {
		fmt.Println("Left conditions are true. Right conditions are False")
	} else {
		fmt.Printf("string with no newline")
		fmt.Println() // empty line
	}

	////////////////////////////////////////////////////////////////////////////
	// Loops (break/continue apply)
	////////////////////////////////////////////////////////////////////////////
	for {
		fmt.Println("do infinite loops with a for like this")
		break
	}

	for i := 0; i < 5; i++ {
		fmt.Println("last printed digit is 4:", i)
	}

	for index, value := range tSlice {
		fmt.Println("iterate all elements from an slice/array:", index, value)
	}
	for key, value := range tMap {
		fmt.Println("iterate all elements from a Map:", key, value)
	}

	////////////////////////////////////////////////////////////////////////////
	// Arrays/Slices/Maps manipulation. Slices in Go are tricky (and performant)
	// Check https://ueokande.github.io/go-slice-tricks/ for more advanced tips
	////////////////////////////////////////////////////////////////////////////
	firstElement := tSlice[0]
	lastElement := tSlice[len(tSlice)-1]            // no negative index
	firstAndSecond := tSlice[0:2]                   // sub-slice syntax: from:to(exclusive).
	firstAndSecond[0] = 55                          // THERE IS NO ALLOCATION, SAME DATA !!!
	fmt.Println(tSlice[0], "==", firstAndSecond[0]) // THERE IS NO ALLOCATION, SAME DATA !!!
	elementIndex := -1                              // there is no function for finding elements
	for i, v := range tSlice {
		if v == 3 {
			elementIndex = i
			break
		}
	} // just do it yourself (as everything else in Go)
	if v, found := tMap["hello"]; found { // finding keys in Maps
		fmt.Println(v)
	}

	tSlice = append(tSlice, 42)     // appending elements to a Slice
	tSlice = tSlice[:len(tSlice)-1] // reslice the Slice after getting last item ==> emulate pop()
	lengthOfSlice := len(tSlice)

	tMap["new key"] = 42    // insert new keys
	delete(tMap, "new key") // remove keys from Map

	// Find elements in a Slice by implementing a for loop
	// Find keys in a Map by implementing a for loop
	// Find values in a Map by implementing a for loop

	////////////////////////////////////////////////////////////////////////////
	// Regex usage
	////////////////////////////////////////////////////////////////////////////

	re := regexp.MustCompile(`[a-z]+`)                             // compile regex expressions before
	_ = re.FindAllString("ab3 c22 dd5", -1)                        // ["ab", "c", "dd"]
	_ = regexp.MustCompile(`\+1[0-9]{7}`).MatchString("+12345678") // true
	_ = regexp.MustCompile(`>([a-z]+)<`).FindStringSubmatch(
		"<123>abcd</123>")[1] // abcd

	////////////////////////////////////////////////////////////////////////////
	// You MUST use every declared variable
	fmt.Println(tBool, tStr, tInt, tFloat, structVar, tNil, tSlice, tMap, powered,
		modDivision, floored, ceiled, roundedStr, rounded, newInt, c, formattedString,
		stringLengthBytes, stringLength, tPointer, firstElement, lastElement,
		firstAndSecond, elementIndex, tSlice, lengthOfSlice)
}
