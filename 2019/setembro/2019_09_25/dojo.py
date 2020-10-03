def main(start, end, divisor):
	days = get_days(start, end)
	count = 0
	for day in days:
		if is_beatiful_day(day, divisor):
			count += 1
	return count 

def get_days(start, end):
	return list(range(start, end + 1))

def invert_number(number):
	return int(str(number)[::-1])

def is_beatiful_day(day, divisor):
	inverted = invert_number(day)
	return (day - inverted) % divisor == 0