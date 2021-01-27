def main():
	return True

def walk_matrix(matrix, direction, border):

	for linha in range(border[1],border[3]):

	# if direction == "UP":
	# 	return [ (1,0) ]
	# if direction == "DOWN":
	# 	return [ (1,2), (2,2) ]
	# if direction == "LEFT":
	# 	return [ (2,1), (2,0) ]
	# return [ (0,0), (0,1), (0,2) ]
    
# def walk_matrix(matrix, direction, border):
#     if direction == "RIGHT":
#         return [ (border[1], x) for x in range(border[0],border[2]) ]
#     if direction == "DOWN":
#         return [ (x, border[2]) for x in range(border[1],border[3]) ]
#     if direction == "LEFT":
#         return [ (border[3], x) for x in range(border[2],border[0],-1) ]
#     if direction == "DOWN":
#         return [ (border[4], x) for x in range(border[3],border[1]) ]

