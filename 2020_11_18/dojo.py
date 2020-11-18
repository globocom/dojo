def split_shoe(shoe):
	att = shoe.split(" ")
	return [int(att[0]), att[1]]


def check_shoe(show_list):
	old_box = []
	counter = 0
	for boot in show_list:
		
		size, direction = split_shoe(boot)
		if direction == "E":
			aux = "D"
		elif direction == "D":
			aux = "E"

		if [size, aux] not in old_box:
			old_box.append([size, direction])
		else:
			old_box.remove([size, aux])
			counter += 1
	
	return counter

		

	# if array == ["38 E"]:
	# 	return 0
	# if array == ["38 E", "38 E", "40 D", "38 D", "40 D", "37 E"] :
	# 	return 6
	# return 2
# array
# p/ cada size do array
# verificar se o oposto tá na lista
# se tiver, tira da lista e n coloca ele na lista, add +1
# se n tiver, coloca ele na lista e segue