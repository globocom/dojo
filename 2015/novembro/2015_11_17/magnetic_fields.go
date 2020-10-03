package magneticFields

import "math"

type Cursor struct {
	x int
	y int
}

type MagneticField struct {
	x      int
	y      int
	radius int
}

func StartingPoint(magneticFields []MagneticField, cursor Cursor) Cursor {
	size := len(magneticFields)
	distances := make([]float64, size, size)
	minorDistance := 9999.0
	var minorMagneticField MagneticField

	for i := 0; i < len(magneticFields); i++ {
		distances[i] = distance(magneticFields[i], cursor)
		if minorDistance > distances[i] {
			minorDistance = distances[i]
			minorMagneticField = magneticFields[i]
		}
	}

	if insideRadius(minorMagneticField, cursor) {
		return Cursor{x: minorMagneticField.x, y: minorMagneticField.y}
	} else {
		return cursor
	}

}

func insideRadius(magneticField MagneticField, cursor Cursor) bool {
	return distance(magneticField, cursor) < float64(magneticField.radius)
}

func distance(magneticField MagneticField, cursor Cursor) float64 {
	return math.Sqrt(math.Pow(float64(cursor.x-magneticField.x), 2.0) + math.Pow(float64(cursor.y-magneticField.y), 2.0))
}
