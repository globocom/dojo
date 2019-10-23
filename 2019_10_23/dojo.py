def check_token(string, token):
	return f' {token} ' in string

def replace_target(string, target, token):
	return string.replace(target, token)

def main(lines):
	result = []
	for line in lines:
		if check_token(line, '&&'):
			line = replace_target(line, '&&', 'and')
		if check_token(line, '||'):
			line = replace_target(line, '||', 'or')
		result.append(line)
	return result