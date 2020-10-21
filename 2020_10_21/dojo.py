#            --- Depois de refatorar ---
def is_decreasing(i, j, k):
	return i > j and j > k

def is_increasing(i, j, k):
	return i < j and j < k

def main(soldiers):
	count = 0
	for i in range(len(soldiers)):
		for j in range(i+1,len(soldiers)):
			for k in range(j+1,len(soldiers)):
				if is_decreasing(soldiers[i],soldiers[j],soldiers[k]) or is_increasing(soldiers[i],soldiers[j],soldiers[k]):
					count += 1

	return count		

	
	# if soldiers[1] == 1:
	# 	return 0
	# if soldiers[0] == 2:
	# 	return 3
	# return 4

	#for i in range(len(soldiers))