package dojo

type ponto struct {
	x int
	y int
}

func isPointIn(p1, p2, p3 ponto) bool {
	if p3.x <= p1.x || p3.y >= p1.y || p3.x >= p2.x || p3.y <= p2.y {
		return false
	}
	return true
}

func intersect(p1, p2, p3, p4 ponto) bool {
	if p1.x != p3.x {
		return false
	}

	return true
}
