package dojo

import (
	"fmt"
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
)

func original() map[string]int {
	return map[string]int{
		"metric1": 1,
		"metric2": 2,
		"metric3": 3,
		"metric4": 4,
	}
}

func TestIsPointIn(t *testing.T) {
	assert := assert.New(t)
	assert.Equal(main(), true, "must be true")
}

func TestExampleDeepMap(t *testing.T) {
	m1 := map[string]int{
		"val1": 10,
		"val2": 20,
	}
	m2 := map[string]int{
		"val2": 20,
		"val1": 10,
	}
	// m1 and m2 are the maps we want to compare
	eq := reflect.DeepEqual(m1, m2)
	if eq {
		fmt.Println("They're equal.")
	} else {
		fmt.Println("They're unequal.")
	}
}

func TestEqual(t *testing.T) {
	assert := assert.New(t)
	original := original()
	remoteMap := map[string]int{
		"metric1": 1,
		"metric2": 2,
		"metric3": 3,
		"metric4": 4,
	}
	ParseMetrics(&original, remoteMap)
	assert.Equal(original, remoteMap, "must be equal")
}

func TestModifyOneMetric(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric1": 1,
		"metric2": 30,
		"metric3": 3,
		"metric4": 4,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "must be equal")
}
func TestModifyTwoMetrics(t *testing.T)               {}
func TestModifyAllMetrics(t *testing.T)               {}
func TestModifyAllMetricsDifferentOrder(t *testing.T) {}
func TestModifyAllMetricsPlusOne(t *testing.T)        {}
func TestModifyAllMetricsPlusTwo(t *testing.T)        {}
func TestRemoveOneMetric(t *testing.T)                {}
func TestRemoveTwoMetrics(t *testing.T)               {}
func TestManyDifferentMetrics(t *testing.T)           {}
