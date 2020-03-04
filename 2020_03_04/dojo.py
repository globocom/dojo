def parse_input(time):
	parsed_date = time.replace(":", " ")
	parsed_time = parsed_date.split(" ")
	return parsed_time[1:]

def convert_time_to_seconds(hms):
	return int(hms[0])*3600 +  int(hms[1])*60 + int(hms[2])
	
def convert_timestamp_to_seconds(timestamp):
	
	hour =  timestamp[1:3]
	minute = timestamp[3:]
	seconds = int(hour)*3600 + int(minute)*60
	if (timestamp[0]== "-"):
		return seconds*(-1)
	
	return seconds
	
	
	# if timestamp == "-0300":
	# 	return -10800
	# if timestamp == "-0530":
	# 	return -19800
	# return -25200