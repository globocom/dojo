def get_painted_nodes(parents, number, jump):
	painted = set({number})
	cur_node = number
	actual_jump = jump
	while cur_node != 1:
		if (actual_jump == 0):
			painted.add(cur_node)
			actual_jump = jump
		cur_node = parents[cur_node - 2]
		actual_jump -= 1

	if (cur_node == 1 and actual_jump == 0):
		painted.add(cur_node)

	return painted


def get_both_nodes(parents, number_A, jump_A, number_B, jump_B):
	set_A = get_painted_nodes(parents, number_A, jump_A)
	set_B = get_painted_nodes(parents, number_B, jump_B)
	return len(set_A | set_B)

def main(parents, jump_A, jump_B):
	answer = 0.0
	n = len(parents) + 1
	for a in range(1,n+1):
		for b in range(1,n+1): 
			painted_nodes = get_both_nodes(parents, a, jump_A, b, jump_B)
			answer += painted_nodes / (n*n)
	
	return answer