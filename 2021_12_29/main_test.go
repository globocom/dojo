package dojo

import (
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
	assert.Equal(original, remoteMap, "Should not modify anything")
}

func TestModifyOneMetric(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric1": 1,
		"metric3": 3,
		"metric2": 30,
		"metric4": 4,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change 1 metric")
}
func TestModifyTwoMetrics(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric1": 10,
		"metric2": 30,
		"metric3": 3,
		"metric4": 4,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change 2 metrics")

}
func TestModifyAllMetrics(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric1": 10,
		"metric2": 30,
		"metric3": 25,
		"metric4": 42,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change all metrics")
}
func TestModifyAllMetricsDifferentOrder(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric3": 25,
		"metric1": 10,
		"metric4": 42,
		"metric2": 30,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change all metrics on a different order")
}
func TestModifyAllMetricsPlusOne(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric3": 25,
		"metric1": 10,
		"metric4": 42,
		"metric2": 30,
		"metric5": 50,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change all metrics and add one")
}
func TestModifyAllMetricsPlusTwo(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric3": 25,
		"metric1": 10,
		"metric4": 42,
		"metric2": 30,
		"metric5": 50,
		"metric6": 600,
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change all metrics and add one")

}
func TestRemoveOneMetric(t *testing.T) {
	assert := assert.New(t)
	original := original()
	remoteMap := map[string]int{
		"metric2": 2,
		"metric3": 3,
		"metric4": 4,
	}
	ParseMetrics(&original, remoteMap)
	assert.Equal(original, remoteMap, "Should remove one metric")
}

func TestRemoveTwoMetrics(t *testing.T) {
	assert := assert.New(t)
	original := original()
	remoteMap := map[string]int{
		"metric3": 3,
		"metric4": 4,
	}
	ParseMetrics(&original, remoteMap)
	assert.Equal(original, remoteMap, "Should remove 2 metrics")
}

func TestManyDifferentMetrics(t *testing.T) {
	assert := assert.New(t)
	org := original()
	remoteMap := map[string]int{
		"metric3":    25,
		"metric2":    30,
		"metric5":    50,
		"metric6":    60,
		"metric9000": 9001, //over 9000
	}

	ParseMetrics(&org, remoteMap)
	assert.Equal(org, remoteMap, "Should change all metrics and add two")
}
