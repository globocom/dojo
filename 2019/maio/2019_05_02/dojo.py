def clear_string(expression):
	result = expression.replace(" ", "")
	result = result.replace("(", "")
	result = result.replace(")", "")
	return result 

def calc(equation, signal):
	parcelas = equation.split(signal)
	result = int(parcelas[0])
	parcelas = parcelas[1:]
	for parcela in parcelas:
		if signal == "+":
			result += int(parcela)
		else:
			result -= int(parcela)


	return result