def is_substring_valid(substring:str) -> bool:

	count_l = substring.count("L")
	count_r = substring.count("R")

	# for letter in substring:
	# 	if letter == "L":
	# 		count_l = count_l + 1
	# 	if letter == "R":
	# 		count_r = count_r + 1

	return count_l == count_r


def main(s:str) -> int:
	subs = ""
	count = 0
	for i in s:
		subs += i
		if is_substring_valid(subs):
			count += 1
			subs =""
	return count
