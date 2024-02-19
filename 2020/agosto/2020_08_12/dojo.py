def get_last_day(final_day, bus):
	return final_day - (final_day % bus)

def call_buses(final_day, buses):
	for bus in buses[::-1]:
		final_day = get_last_day(final_day, bus)

	return final_day