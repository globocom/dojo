def get_position(initial_position, distance, qnt_jumps):
	return initial_position + distance * qnt_jumps

def main(cang1_position, cang1_distance, cang2_position, cang2_distance):
	count = 0
	cang1Pos = get_position(cang1_position, cang1_distance, count)
	cang2Pos = get_position(cang2_position, cang2_distance, count)

	if cang1Pos == cang2Pos:
		return True

	while cang2Pos > cang1Pos:
		count = count + 1
		cang1Pos = get_position(cang1_position, cang1_distance, count)
		cang2Pos = get_position(cang2_position, cang2_distance, count)
		if cang1Pos == cang2Pos:
			return True
	return False
		